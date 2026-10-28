
const form = document.getElementById("predictionForm");
const predictButton = document.getElementById("predictButton");
const buttonText = document.getElementById("buttonText");
const errorMessage = document.getElementById("errorMessage");
const resultCard = document.getElementById("resultCard");
const predictedPrice = document.getElementById("predictedPrice");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    errorMessage.hidden = true;
    resultCard.hidden = true;

    if (!form.reportValidity()) {
        return;
    }

    const formData = new FormData(form);

    const payload = {
        longitude: Number(formData.get("longitude")),
        latitude: Number(formData.get("latitude")),
        housing_median_age: Number(formData.get("housing_median_age")),
        total_rooms: Number(formData.get("total_rooms")),
        total_bedrooms: Number(formData.get("total_bedrooms")),
        population: Number(formData.get("population")),
        households: Number(formData.get("households")),
        median_income: Number(formData.get("median_income")),
        ocean_proximity: formData.get("ocean_proximity")
    };

    const numericValues = [
        payload.longitude,
        payload.latitude,
        payload.housing_median_age,
        payload.total_rooms,
        payload.total_bedrooms,
        payload.population,
        payload.households,
        payload.median_income
    ];

    if (!numericValues.every(Number.isFinite)) {
        showError("Please enter valid numeric values in every field.");
        return;
    }

    if (payload.total_bedrooms > payload.total_rooms) {
        showError("Total bedrooms cannot exceed total rooms.");
        return;
    }

    predictButton.disabled = true;
    buttonText.textContent = "Calculating estimate...";

    try {
        const response = await fetch("/api/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(payload)
        });

        // Read as text first to avoid JSON parsing errors on empty responses.
        const responseText = await response.text();

        if (!responseText.trim()) {
            throw new Error(
                "The server returned an empty response. Please restart the backend."
            );
        }

        let data;

        try {
            data = JSON.parse(responseText);
        } catch {
            throw new Error(
                "The server response was not valid JSON. Check the backend terminal."
            );
        }

        if (!response.ok) {
            throw new Error(
                data.detail || data.error ||
                `Prediction failed (HTTP ${response.status}).`
            );
        }

        if (
            typeof data.predicted_price !== "number" ||
            !Number.isFinite(data.predicted_price)
        ) {
            throw new Error("The server did not return a valid predicted price.");
        }

        predictedPrice.textContent = new Intl.NumberFormat("en-US", {
            style: "currency",
            currency: "USD",
            maximumFractionDigits: 0
        }).format(data.predicted_price);

        resultCard.hidden = false;
        resultCard.scrollIntoView({
            behavior: "smooth",
            block: "nearest"
        });

    } catch (error) {
        showError(
            error.message ||
            "Unable to connect to the prediction server. Make sure app.py is running."
        );
    } finally {
        predictButton.disabled = false;
        buttonText.textContent = "Estimate home value";
    }
});

form.addEventListener("reset", function () {
    errorMessage.hidden = true;
    resultCard.hidden = true;
});

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.hidden = false;
}

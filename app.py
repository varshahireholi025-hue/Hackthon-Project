from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Crop data API
@app.route('/data')
def get_data():
    crop = request.args.get("crop", "Unknown")

    sample_data = {
        "Maize":  {"price": 1800, "live_price": 1850, "district": "Belagavi"},
        "Wheat":  {"price": 2200, "live_price": 2300, "district": "Belagavi"},
        "Rice":   {"price": 2500, "live_price": 2600, "district": "Belagavi"}
    }

    if crop in sample_data:
        return jsonify({
            "crop": crop,
            "price": sample_data[crop]["price"],
            "live_price": sample_data[crop]["live_price"],
            "district": sample_data[crop]["district"]
        })
    else:
        return jsonify({"error": "Invalid crop name"}), 400


# Send API (Button on top)
@app.route('/send', methods=['POST'])
def send_crop():
    data = request.get_json()
    crop = data.get("crop", None)

    return jsonify({"message": f"Crop '{crop}' received by backend!"})


if __name__ == '__main__':
    app.run(debug=True)
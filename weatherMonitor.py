import forecastio

api_key = "0d410c63644aaf64cb3755ee67bc8bc2"
lat = -31.967819
lng = 115.87718

forecast = forecastio.load_forecast(api_key, lat, lng)

print forecast.hourly()
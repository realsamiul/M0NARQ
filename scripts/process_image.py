import numpy as np
import rasterio
import matplotlib.pyplot as plt

class SatelliteImageProcessor:
    def __init__(self, red_band_path, nir_band_path, night_light_path):
        self.red_band_path = red_band_path
        self.nir_band_path = nir_band_path
        self.night_light_path = night_light_path

    def calculate_ndvi(self):
        try:
            with rasterio.open(self.red_band_path) as red:
                red_data = red.read(1)
            with rasterio.open(self.nir_band_path) as nir:
                nir_data = nir.read(1)

            ndvi = (nir_data - red_data) / (nir_data + red_data)
            return ndvi
        except Exception as e:
            print(f"Error calculating NDVI: {e}")
            return None

    def flood_detection(self, threshold=0.3):
        try:
            ndvi = self.calculate_ndvi()
            if ndvi is None:
                return None
            flooded_areas = ndvi < threshold
            return flooded_areas
        except Exception as e:
            print(f"Error in flood detection: {e}")
            return None

    def urban_analysis(self):
        # Placeholder for urban analysis logic
        print("Urban analysis not implemented yet.")

    def night_light_processing(self):
        try:
            with rasterio.open(self.night_light_path) as night_light:
                night_light_data = night_light.read(1)
            # Placeholder for night light processing logic
            return night_light_data
        except Exception as e:
            print(f"Error processing night light data: {e}")
            return None

if __name__ == '__main__':
    processor = SatelliteImageProcessor('path_to_red_band.tif', 'path_to_nir_band.tif', 'path_to_night_light.tif')
    ndvi_result = processor.calculate_ndvi()
    if ndvi_result is not None:
        plt.imshow(ndvi_result, cmap='RdYlGn')
        plt.colorbar()
        plt.title('NDVI Result')
        plt.show()
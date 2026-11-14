import os
import sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
from data.loader import HyperspectralDataLoader, SEVERITY_MAPPING, get_wavelength_grid
from data.validator import DataValidator
from preprocessing.spectral_reader import SpectralReader

def test_dashboard_backend():
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "data", "raw", "tomato_wilt", "Tomato bacterial wilt dataset"))
    
    loader = HyperspectralDataLoader(data_dir)
    df_meta = loader.scan_dataset()
    print(f"Dashboard backend scanned: {len(df_meta)} samples.")
    assert len(df_meta) == 293
    
    # Test loading and processing Level0 sample
    l0_row = df_meta[df_meta["severity_level"] == 0].iloc[0]
    spe_l0 = SpectralReader.load_from_mat(l0_row["avg_file"])
    val_l0 = DataValidator.validate_spectrum(spe_l0)
    indices_l0 = SpectralReader.calculate_vegetation_indices(spe_l0)
    
    print(f"Specimen {l0_row['sample_id']}: Validation={val_l0['valid']}, NDVI={indices_l0['NDVI']:.3f}, CI={indices_l0['CI_green']:.2f}")
    assert val_l0["valid"] is True
    assert "NDVI" in indices_l0
    
    # Test loading and processing Level4 sample
    l4_row = df_meta[df_meta["severity_level"] == 4].iloc[0]
    spe_l4 = SpectralReader.load_from_mat(l4_row["avg_file"])
    val_l4 = DataValidator.validate_spectrum(spe_l4)
    indices_l4 = SpectralReader.calculate_vegetation_indices(spe_l4)
    
    print(f"Specimen {l4_row['sample_id']}: Validation={val_l4['valid']}, NDVI={indices_l4['NDVI']:.3f}, CI={indices_l4['CI_green']:.2f}")
    assert val_l4["valid"] is True
    assert indices_l0["NDVI"] > indices_l4["NDVI"]
    
    print("\nDASHBOARD BACKEND INTEGRATION TEST PASSED!")

if __name__ == "__main__":
    test_dashboard_backend()


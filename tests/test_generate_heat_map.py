import geopandas as gpd
from shapely.geometry import Point
import geopandas.testing as gpd_testing
from src.generate_heat_map import *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

def test_load_consumption_data(mocker):
    fake_gdf = gpd.GeoDataFrame()
    mock_read_parquet = mocker.patch("src.generate_heat_map.gpd.read_parquet", return_value=fake_gdf)
    bbox = [0, 0, 1, 1]
    result = load_consumption_data(bbox)

    assert result is fake_gdf
    mock_read_parquet.assert_called_once_with(
        "s3://weave.energy/smart-meter",
        bbox=bbox,
        columns=[
            "geometry",
            "data_collection_log_timestamp",
            "total_consumption_active_import",
            "secondary_substation_unique_id"
        ],
        filters=[("data_collection_log_timestamp", "=", pd.Timestamp("2024-07-14 20:00Z"))]
    )

def test_aggregate_substation_data():
    input_data = {
        "secondary_substation_unique_id": ["A", "A", "B"],
        "geometry": [Point(0, 0), Point(0, 0), Point(1, 1)],
        "total_consumption_active_import": [1000, 1500, 1800]
    }
    input_gdf = gpd.GeoDataFrame(input_data, geometry="geometry")
    expected_data = {
        "secondary_substation_unique_id": ["A", "B"],
        "geometry": [Point(0, 0), Point(1, 1)],
        "total_consumption_active_import": [2.5, 1.8] 
    }
    expected_gdf = gpd.GeoDataFrame(expected_data, geometry="geometry")
    result_gdf = aggregate_substation_data(input_gdf)

    gpd_testing.assert_geodataframe_equal(
        result_gdf,
        expected_gdf,
        check_like=True
    )
def test_plot_heatmap_is_not_none():
    data = {
        "secondary_substation_unique_id": ["A", "B"],
        "geometry": [Point(0, 0), Point(1, 1)],
        "total_consumption_active_import": [2.5, 1.8],
    }
    gdf = gpd.GeoDataFrame(data)
    gdf = gdf.set_geometry("geometry")
    fig = plot_heatmap(gdf, "Test Title")
    assert fig is not None
    assert isinstance(fig, Figure)

def test_generate_base64_image():
    fig, _ = plt.subplots()
    img_data = generate_base64_image(fig)

    assert img_data.startswith("data:image/png;base64,")
    assert len(img_data) > len("data:image/png;base64,")


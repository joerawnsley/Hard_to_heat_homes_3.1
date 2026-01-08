let map;

function initMap() {
    const firstProp = mapData.props[0];
    map = L.map("map").setView([51.463907, -2.584353], 17);

    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: "&copy; OpenStreetMap",
    }).addTo(map);

    fetch("static/data/bristol_usrn_polygons.json")
        .then((response) => response.json())
        .then((data) => {
            L.geoJSON(data, {
                style: function(feature) {
                    switch (feature.properties.average_epc_score) {
                        case 61: 
                            return {
                                color: "#1bb558",
                                weight: 2,
                            }
                        case 70: 
                            return {
                                color: "#fcaa64",
                                weight: 2,
                            }
                        case null: 
                            return {
                                color: "#9b9b9bd0",
                                weight: 2,
                            }
                        }
                    },
                onEachFeature: function (feature, layer) {
                    epc_score = feature.properties.average_epc_score
                        ? feature.properties.average_epc_score
                        : "unknown";
                    layer.bindPopup(
                        "Number of buildings: 30" +
                            "<br>" +
                        "Address: " +
                            feature.properties.address +
                            "<br>" +
                        "Postcode: " +
                            feature.properties.postcode +
                            "<br>" +
                        "Average EPC Score: " +
                            epc_score
                    );
                },
            }).addTo(map);
        });
}

document.addEventListener("DOMContentLoaded", () => {
    initMap();
});

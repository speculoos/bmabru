/*
 *  wms.config.js
 */

var WMS_CONFIG = {
    'CIRB WMS':{
        url: 'http://geoserver.gis.irisnet.be/geoserver/wms',
        options:{
            layers: 'urbis:URB_A_BU',
            format: 'image/png',
            transparent: true,
            attribution: "Brugis GeoWebCache"
        }
    },
    'bMa/OSM':{
        url: 'http://bmawms.specgis.be/service',
        options:{
            layers: 'bMa',
            format: 'image/png',
            transparent: true,
            attribution: "OpenStreetMap styled by Speculoos"
        }
    },
};
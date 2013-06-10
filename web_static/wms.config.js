/*
 *  wms.config.js
 */

var MAP_CONFIG = 
{
//     http://www.cirb.irisnet.be/catalogue-de-services/urbis/services-urbis-1/urbis-wms-et-wmts
    CENTER:[50.854075572144815, 4.38629150390625],
    ZOOM: 13,
    CRS:L.CRS.EPSG900913,
    WMS:{
        'Urbis bâtiments':{
            url: 'http://geoserver.gis.irisnet.be/geoserver/wms',
            options:{
                layers: 'urbis:URB_A_BU',
                format: 'image/png',
                transparent: true,
                attribution: "Brugis GeoWebCache"
            }
        },
        
        'Urbis shapes':{
            url: 'http://geoserver.gis.irisnet.be/geoserver/wms',
            options:{
                layers: 'urbis:URB_M_SHAPE',
                format: 'image/png',
                transparent: true,
                attribution: "Brugis GeoWebCache"
            }
        },
    

        'bMa (OSM)':{
            url: 'http://bmawms.specgis.be/service',
            visible: true,
            options:{
                layers: 'bMa',
                format: 'image/png',
                    transparent: true,
                    attribution: "OpenStreetMap styled by Speculoos"
            }
        },
    }
};
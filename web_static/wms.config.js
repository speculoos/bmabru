/*
 *  wms.config.js
 */

var WMS_CONFIG = {
    
    'bMa (on Open Street Map)':{
        url: 'http://bmawms.specgis.be/service',
        options:{
            layers: 'bMa',
            format: 'image/png',
                transparent: true,
                attribution: "OpenStreetMap styled by Speculoos"
        }
},

//     http://www.cirb.irisnet.be/catalogue-de-services/urbis/services-urbis-1/urbis-wms-et-wmts

    'Urbis':{
    url: 'http://geoserver.gis.irisnet.be/geoserver/wms',
    options:{
        layers: 'urbis:urbisFR',
        format: 'image/png',
            transparent: true,
            attribution: "Brugis GeoWebCache"
    }
    
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
  
    'Urbis topo lines':{
        url: 'http://geoserver.gis.irisnet.be/geoserver/wms',
        options:{
            layers: 'urbis:URB_T_LINE',
            format: 'image/png',
                transparent: true,
                attribution: "Brugis GeoWebCache"
        }
    },
    
    
};
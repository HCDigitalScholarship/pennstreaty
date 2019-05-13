$(document).ready(function() {
    //initPage(pageID);
    var page = document.getElementById('call_the_dragon');
    var pageID = page.getAttribute('data-id');
    console.log(pageID);
    if (pageID < 1 && pageID > lastpage) {
        alert("Page out of range.");
    } else {
        $("#openseadragon1").html("");
        var viewer = OpenSeadragon({
            id: "openseadragon1",
            prefixUrl: "//openseadragon.github.io/openseadragon/images/",
//          tileSources: "/srv/QI/static/img/Misc_mss_1791_06_02_001.dzi",
//            tileSources: "http://104.131.45.60/img/Misc_mss_1791_06_02_001.dzi"
            tileSources: "http://104.131.45.60/img/"+ pageID+ ".dzi"
//          tileSources: duomo
/*            showNavigator: true,
            navigatorPosition: "ABSOLUTE",
            navigatorTop: "40px",
            navigatorLeft: "4px",
            navigatorHeight: "110px",
            navigatorWidth: "90px",
            sequenceMode: true,
            showReferenceStrip: true,
            referenceStripScroll: 'horizontal',*/
        });
    }
    // This controls what happens when someone uses the close button.
});


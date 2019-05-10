pageID = Math.floor(Page_id);
function initPage(newPageID) {
    if (pageID >= 1 && pageID <= lastpage) {
        pageID = newPageID;
        if (pageID < 10) {
            var newstring = "00" + pageID.toString(); // turn this into string
        } else if (pageID < 100) {
            var newstring = "0" + pageID.toString();
        } else {
            var newstring = pageID.toString();
        }
        var newImgUrl = Manuscript_id + "_" + newstring;
        // Load the image and the transcription
        $('#imgDiv img').remove();
        $('#imgDiv').append("<img src =/static/img/" + newImgUrl + ".jpg></div>");
/*        $.get("/pagetranscription/" + newImgUrl, function (data) {
            $("#transcriptionDiv").html(data).promise().done(initLinks);
        });*/
        window.history.pushState("Page Information", "Page Information", "/transcribepage/" + newImgUrl + "/");
    } else {
        alert("Page out of range.");
    }
}
function inPage(newID){
    if(pageID >= 1 && pageID <= lastpage){
	pageID = newID;
	if (pageID < 10) {
            var newstring = "00" + pageID.toString(); // turn this into string
        } else if (pageID < 100) {
            var newstring = "0" + pageID.toString();
        } else {
            var newstring = pageID.toString();
        }
        var newImgUrl = Manuscript_id + "_" + newstring;
    }
    return newImgUrl;
}

/*$(document).ready(function() {
    //initPage(pageID);
    if (pageID < 1 && pageID > lastpage) {
	alert("Page out of range.");
    } else {
    	$("#openseadragon1").html("");
    	var viewer = OpenSeadragon({
            id: "openseadragon1",
            prefixUrl: "//openseadragon.github.io/openseadragon/images/",
            showNavigator: true,
            navigatorPosition: "ABSOLUTE",
            navigatorTop: "40px",
            navigatorLeft: "4px",
            navigatorHeight: "110px",
            navigatorWidth: "90px",
            sequenceMode: true,
            showReferenceStrip: true,
            referenceStripScroll: 'horizontal',
    	});
    }
    // This controls what happens when someone uses the close button.
    $("i.fa.fa-times").click(function() {
        $('.off-canvas').animate({
            "margin-right": '-=25%'
        });
        $('i.fa.fa-times').animate({
            "margin-right": '-=25%'
        });
        $('.off-canvas div').remove();
    });
    // Go forward in the image viewer.
    $(".forwards-arrow i.fa.fa-chevron-right").click(function() {
        initPage(pageID + 1);
	location.reload();
    });
    // Go backward in the image viewer.
    $(".forwards-arrow i.fa.fa-chevron-left").click(function() {
        initPage(pageID - 1);
	location.reload();
    });
});*/

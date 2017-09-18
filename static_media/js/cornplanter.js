console.log("BLEH");
$(document).ready(function() {
    console.log('Got here');
    var newPage_id = Page_id;
    // set page_id (as an int) to a global variable to use later
    window.Page_id = Math.floor(Page_id); 
    // for example, "003" becomes 3
    console.log(window.Page_id);
    console.log(Manuscript_id);
    console.log(lastpage);
    $.ajax({
        url: '/manuscriptinfo/' + Manuscript_id,
        type: 'GET',
        dataType: 'json',
        cache: true,
        success: callback_3,
        error: function(data) {
            console.log("not quite");
        }
    });
    function callback_3(data) {
        //$(".off-canvas-content-meta").append("<div><h3>Metadata</h3><span class='meta-title'> Name of Document </span> <p>" + data[0]["fields"].title + "</p> <span class='meta-title'> Creator </span><p> " + data[0]["fields"].person_id + "</p><span class='meta-title'> Date </span><p> " + data[0]["fields"].date + "</p> <span class='meta-title'> Type of Document </span> <p>" + data[0]["fields"].type_of_Manuscript + "</p><span class='meta-title'> Call Number </span><p> " + data[0]["fields"].call_no + "</p></div>");
        var imgurl = Manuscript_id + "_" + newPage_id
        console.log(Page_id);
        console.log(imgurl);
        $('#imgDiv').append("<img src =/static/img/" + imgurl + ".jpg>");
        $.get("/pagetranscription/" + imgurl, function (data) {
	    $("#transcriptionDiv").html(data);
        });
    }
    // this is the function that will be run through every time a persName, orgName, placeName a href is clicked in the transcription
    // this is the original function
    $("a").click(function() {
        console.log('you clicked on something');
        var href = $(this).attr('href');
        var newhref = href.slice(1, href.length);
        $.ajax({
            url: '/something/' + newhref,
            type: 'GET',
            dataType: 'json',
            cache: true,
            success: callback_2,
            error: function(data) {
                console.log("not quite");
            }
        });
        // all the conditions for when someone either clicks a name, or the close button, or another
	// name without closing the first slideout
        function callback_2(data) {
            console.log(data[0]);
            console.log(newhref);
            if (data[0]["model"] == "QI.person") {
                if (data[0]["fields"].birth_date == "") {
                    data[0]["fields"].birth_date = 'Unknown'
                }
                if (data[0]["fields"].death_date == "") {
                    data[0]["fields"].death_date = 'Unknown'
                }
                if (data[0]["fields"].other_names == "") {
                    data[0]["fields"].other_names = 'None'
                }
                if (data[0]["fields"].bio_notes == "") {
                    data[0]["fields"].bio_notes = 'None'
                }
                //start (#1)
                if (($('.off-canvas div').attr('id')) == undefined) {
                    console.log("its happening!");
                    $('.off-canvas').append("<div id = " + newhref + "><br /><h3>Person Information</h3><span> Name </span><p> " + data[0]["fields"].first_name + " " + data[0]["fields"].last_name + "</p><span> Birth Date </span> <p>" + data[0]["fields"].birth_date + "</p> <span> Death Date</span> <p> " + data[0]["fields"].death_date + "</p> <span> Notes </span><p> " + data[0]["fields"].bio_notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].other_names + "</p> <span><a href=/person/" + data[0]["fields"].id_tei + "> &rarr; View more information</a></span><p> </div>");
                    $('.off-canvas').animate({
                        "margin-right": '+=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '+=25%'
                    });
                } else if (newhref == ($('.off-canvas div').attr('id'))) {
                    $('.off-canvas').animate({
                        "margin-right": '-=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '-=25%'
                    });
                    $('.off-canvas div').remove();
                } else {
                    // this is the case when you click on another (different) a href right after clicking a first one
                    $('.off-canvas').animate({
                        "margin-right": '-=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '-=25%'
                    });
                    $('.off-canvas div').remove();
                    $('.off-canvas').append("<div id = " + newhref + "><br /><h3>Person Information</h3><span> Name </span><p> " + data[0]["fields"].first_name + " " + data[0]["fields"].last_name + "</p><span> Birth Date </span> <p>" + data[0]["fields"].birth_date + "</p> <span> Death Date</span> <p> " + data[0]["fields"].death_date + "</p> <span> Notes </span><p> " + data[0]["fields"].bio_notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].other_names + "</p> <span><a href=/person/" + data[0]["fields"].id_tei + "> &rarr; View more information</a></span><p> </div>");
                    $('.off-canvas').animate({
                        "margin-right": '+=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '+=25%'
                    });

                }
            } else if (data[0]["model"] == "QI.place") {
                if (data[0]["fields"].county == "") {
                    data[0]["fields"].county = 'Unknown';
                }
                if (data[0]["fields"].state == "") {
                    data[0]["fields"].state = 'Unknown';
                }
                if (data[0]["fields"].latitude == "") {
                    data[0]["fields"].latitude = 'Unknown';
                } else {
                    data[0]["fields"].latitude = data[0]["fields"].latitude + " N"
                    data[0]["fields"].longitude = data[0]["fields"].longitude + " W"
                }
                if (data[0]["fields"].notes == "") {
                    data[0]["fields"].notes = 'None';
                }
                if (data[0]["fields"].alternate == "") {
                    data[0]["fields"].alternate = 'None';
                }
                if (($('.off-canvas div').attr('id')) == undefined) {
                    $('.off-canvas').append("<div id = " + newhref + "><br /><h3>Place Information</h3><span> Name </span><p> " + data[0]["fields"].name + "</p><span> County </span> <p>" + data[0]["fields"].county + "</p> <span> State </span> <p> " + data[0]["fields"].state + "</p> <span> Location </span> <p>" + data[0]["fields"].latitude + " " + data[0]["fields"].longitude + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].alternate + "</p> <span><a href=/place/" + data[0]["fields"].id_tei + "> &rarr; View more information</a></span><p> </div>");
                    $('.off-canvas').animate({
                        "margin-right": '+=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '+=25%'
                    });
                } else if (newhref == ($('.off-canvas div').attr('id'))) {
                    $('.off-canvas').animate({
                        "margin-right": '-=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '-=25%'
                    });
                    $('.off-canvas div').remove();
                } else {
                    // this is the case when you click on another (different) a href right after clicking a first one
                    $('.off-canvas').animate({
                        "margin-right": '-=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '-=25%'
                    });
                    $('.off-canvas div').remove();
                    $('.off-canvas').append("<div id = " + newhref + "><br /><h3>Place Information</h3><span> Name </span><p> " + data[0]["fields"].name + "</p><span> County </span> <p>" + data[0]["fields"].county + "</p> <span> State </span> <p> " + data[0]["fields"].state + "</p> <span> Location </span> <p>" + data[0]["fields"].latitude + " " + data[0]["fields"].longitude + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].alternate + "</p> <span><a href=/place/" + data[0]["fields"].id_tei + "> &rarr; View more information</a></span><p> </div>");
                    $('.off-canvas').animate({
                        "margin-right": '+=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '+=25%'
                    });
                }
            } else {
                if (data[0]["fields"].date_founded == "") {
                    data[0]["fields"].date_founded = 'Unknown';
                }
                if (data[0]["fields"].date_dissolved == "") {
                    data[0]["fields"].date_dissolved = 'Unknown';
                }
                if (data[0]["fields"].notes == "") {
                    data[0]["fields"].notes = 'Unknown';
                }
                if (data[0]["fields"].associated_spellings == "") {
                    data[0]["fields"].associated_spellings = 'None';
                }
                if (data[0]["fields"].other_names == "") {
                    data[0]["fields"].other_names = 'None';
                }
                //start (#1)
                if (($('.off-canvas div').attr('id')) == undefined) {
                    $('.off-canvas').append("<div id = " + newhref + "><br /><h3>Organization Information</h3><span> Name </span><p> " + data[0]["fields"].organization_name + "</p><span> Date Founded </span> <p>" + data[0]["fields"].date_founded + "</p> <span> Date Dissolved </span> <p> " + data[0]["fields"].date_dissolved + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Associated Spellings </span> <p>" + data[0]["fields"].associated_spellings + "</p> <span> Other Names </span> <p>" + data[0]["fields"].other_names + "</p> <span><a href=/org/" + data[0]["fields"].id_tei + "> &rarr; View more information</a></span><p> </div>");
                    $('i.fa.fa-times').animate({
                        "margin-right": '+=25%'
                    });
                    $('.off-canvas').animate({
                        "margin-right": '+=25%'
                    });
                } else if (newhref == ($('.off-canvas div').attr('id'))) {
                    $('.off-canvas').animate({
                        "margin-right": '-=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '-=25%'
                    });
                    $('.off-canvas div').remove();
                } else {
                    //this is the case when you click on another (different) a href right after clicking a first one
                    $('.off-canvas').animate({
                        "margin-right": '-=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '-=25%'
                    });
                    $('.off-canvas div').remove();
                    $('.off-canvas').append("<div id = " + newhref + "><br /><h3>Organization Information</h3><span> Name </span><p> " + data[0]["fields"].organization_name + "</p><span> Date Founded </span> <p>" + data[0]["fields"].date_founded + "</p> <span> Date Dissolved </span> <p> " + data[0]["fields"].date_dissolved + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Associated Spellings </span> <p>" + data[0]["fields"].associated_spellings + "</p> <span> Other Names </span> <p>" + data[0]["fields"].other_names + "</p> <span><a href=/org/" + data[0]["fields"].id_tei + "> &rarr; View more information</a></span><p> </div>");
                    $('.off-canvas').animate({
                        "margin-right": '+=25%'
                    });
                    $('i.fa.fa-times').animate({
                        "margin-right": '+=25%'
                    });
                }
            }
        }
    });
    // this controls what happens when someone uses the close button
    $("i.fa.fa-times").click(function() {
        $('.off-canvas').animate({
            "margin-right": '-=25%'
        });
        $('i.fa.fa-times').animate({
            "margin-right": '-=25%'
        });
        $('.off-canvas div').remove();
    });
    // the below controls how the metadata from off canvas is loaded, and changes the direction of the chevron depending on if you can see the metadata or not
    $(".canvas-meta").click(function() {
        if (($('aside.off-canvas-content-meta').attr("id")) == "open") {
            $('.canvas-meta i').css("transform", "rotate(90deg)");
            $('.canvas-meta p').animate({
                "margin-left": '-=25%'
            });
            $('aside.off-canvas-content-meta').attr("id", "");
            $('.off-canvas-content-meta').animate({
                "margin-left": '-=25%'
            });
        } else {
            $('.canvas-meta i').css("transform", "rotate(270deg)");
            $('.canvas-meta p').animate({
                "margin-left": '+=25%'
            });
            $('aside.off-canvas-content-meta').attr("id", "open");
            $('.off-canvas-content-meta').animate({
                "margin-left": '+=25%'
            });
        }
    });
    // the below controls how the image from off canvas is loaded, and changes the direction of the chevron depending on if you can see the image or not
    $(".canvas-img").click(function() {
        if (($('aside.off-canvas-content-img').attr("id")) == "open") {
            $('.canvas-img i').css("transform", "rotate(90deg)");
            $('.canvas-img p').animate({
                "margin-left": '-=25%'
            });
            $('aside.off-canvas-content-img').attr("id", "");
            $('.off-canvas-content-img').animate({
                "margin-left": '-=25%'
            });
        } else {
            $('.canvas-img i').css("transform", "rotate(270deg)");
            $('.canvas-img p').animate({
                "margin-left": '+=25%'
            });
            $('aside.off-canvas-content-img').attr("id", "open");
            $('.off-canvas-content-img').animate({
                "margin-left": '+=25%'
            });
        }
    });
    // controls going forward in the image viewer
    $(".forwards-arrow i.fa.fa-chevron-right").click(function() {
        if (window.Page_id < lastpage) {
            console.log('nice job');
            window.Page_id = window.Page_id + 1 // increment page number
            if (window.Page_id < 10) {
                var newstring = "00" + window.Page_id.toString(); // turn this into string
            } else if (window.Page_id < 100) {
                var newstring = "0" + window.Page_id.toString();
            } else {
                var newstring = window.Page_id.toString();
            }
            var newImgUrl = Manuscript_id + "_" + newstring;
            console.log(newImgUrl);
            $('#imgDiv img').remove();
	    // Load the image and the transcription
            $('#imgDiv').append("<img src =/static/img/" + newImgUrl + ".jpg></div>");
            console.log('got here!!!');
	    $.get("/pagetranscription/" + newImgUrl, function (data) {
                $("#transcriptionDiv").html(data);
	    });
            window.history.pushState("Page Information", "Page Information", "/page/" + newImgUrl + "/");
        } else {
            alert('This is the last page of this manuscript!');
        }
    });
    // controls going backward in the image viewer
    $(".forwards-arrow i.fa.fa-chevron-left").click(function() {
        if (window.Page_id > 1) {
            console.log('nice!');
            window.Page_id = window.Page_id - 1 // increment page number
            if (window.Page_id < 10) {
                var newstring = "00" + window.Page_id.toString(); // turn this into string
            } else if (window.Page_id < 100) {
                var newstring = "0" + window.Page_id.toString();
            } else {
                var newstring = window.Page_id.toString();
            }
            var newImgUrl = Manuscript_id + "_" + newstring;
	    // Load the image and the transcription
            $('#imgDiv img').remove();
            $('#imgDiv').append("<img src =/static/img/" + newImgUrl + ".jpg></div>");
	    $.get("/pagetranscription/" + newImgUrl, function (data) {
                $("#transcriptionDiv").html(data);
	    });
            window.history.pushState("Page Information", "Page Information", "/page/" + newImgUrl + "/");
        } else {
            alert('This is the first page of this manuscript!');
        }
    });
});

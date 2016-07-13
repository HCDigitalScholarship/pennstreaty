$(document).ready(function() {
  console.log('Got here');
  // this is just to check the script is working
// now we are going to immediately load the metadata and image
//information of the transcription we are viewing into the off canvas divs to the left (meta/img)

var newPage_id = Page_id;
window.Page_id = Math.floor(Page_id); // set page_id (as an int) to a global variable to use later
//for example, "003" becomes 3
console.log(window.Page_id);
console.log(Manuscript_id);
console.log(lastpage);


//$(".off-canvas-content-meta").append("<div><h3>Metadata</h3><span class='meta-title'> Name of Document </span> <p>" + data[0]["fields"].title + "</p> <span class='meta-title'> Creator </span><p> " + data[0]["fields"].person_id + "</p><span class='meta-title'> Date </span><p> " + data[0]["fields"].date + "</p> <span class='meta-title'> Type of Document </span> <p>" + data[0]["fields"].type_of_Manuscript + "</p><span class='meta-title'> Call Number </span><p> " + data[0]["fields"].call_no + "</p></div>");

//var imgurl = Manuscript_id + "_" + newPage_id
//console.log(Page_id);
//console.log(imgurl);
//$('.original-image-wrapper').append("<div><h3>Original Document</h3><img src =/static/img/"+imgurl+".png></div>");


$.ajax({
                  //url: 'https://ds-omeka.haverford.edu/qi/api/items/2635',
                  url: '/manuscriptinfo/' + Manuscript_id,
                  type: 'GET',
                  //dataType: 'jsonp',
                  dataType: 'json',
                  cache: true,
                  success: callback_3,  //call a function to get all metadata in order, get information from omeka
                  error: function(data) { console.log("not quite");}
                })

function callback_3(data) {
 /* --> this was the old function when using omeka data!!
  var metadata_list = {}
  var url_thing = {}
  url_thing = data.data.files.url; //(this will be important soon)
  metadata_list[data.data.id] = data.data.element_texts;

  meta_keys = Object.keys(metadata_list);

    for (var i=0; i<meta_keys.length; i++) {
      my_dict = {}
      for (var j=0; j<metadata_list[meta_keys[i]].length; j++) {
        var type = metadata_list[meta_keys[i]][j].element.name;
        var content = metadata_list[meta_keys[i]][j].text;
        my_dict[type] = content;
      }

    }
// now from the function above, we can easily call on the metadata information we need and
// append it to one of our off canvas divs so it will be there
*/

 //$(".off-canvas-content-meta").append("<div><h3>Metadata</h3><span class='meta-title'> Name of Document </span> <p>" + my_dict["Title"] + "</p> <span class='meta-title'> Creator </span><p> " + my_dict["Creator"] + "</p><span class='meta-title'> Date </span><p> " + my_dict["Date"] + "</p> <span class='meta-title'> Type of Document </span> <p>" + my_dict["Material Type"] + "</p><span class='meta-title'> Call Number </span><p> " + my_dict["Call Number"] + "</p></div>");

//////////// IMPORTANT
 $(".off-canvas-content-meta").append("<div><h3>Metadata</h3><span class='meta-title'> Name of Document </span> <p>" + data[0]["fields"].title + "</p> <span class='meta-title'> Creator </span><p> " + data[0]["fields"].person_id + "</p><span class='meta-title'> Date </span><p> " + data[0]["fields"].date + "</p> <span class='meta-title'> Type of Document </span> <p>" + data[0]["fields"].type_of_Manuscript + "</p><span class='meta-title'> Call Number </span><p> " + data[0]["fields"].call_no + "</p></div>");
 var imgurl = Manuscript_id + "_" + newPage_id
 console.log(Page_id);
 console.log(imgurl);
 $('.original-image-wrapper').append("<div><h3>Original Document</h3><img src =/static/img/"+imgurl+".png></div>");
/////////// IMPORTANT

// LINES 51 to 105 CAN MAYBE BE DELETED????????

/*
$.ajax({
    url: 'https:\/\/ds-omeka.haverford.edu\/qi\/api\/files?item='+Manuscript_id,
    //url: img_url, // this should work? but u should check what form page.img_url is in and whether u need json or jsonp
    type: 'GET',
    dataType: 'jsonp',
    // ?????? is it json or jsonp??? what is this img_url format?
    cache: true,
    success: get_img, //call a function to get image information
    error: function(stuff) { console.log("not quite 2");}
  })
*/

}

/*
function get_img(stuff) { //all image related api info coming from omeka

  var img_list = {}
  var img = {}
  var originals_list = []
  console.log(stuff.data);
  console.log(stuff.data[0]['id']);
  img_keys = Object.keys(stuff.data);
  listofpages = stuff.data;

  for (var a=0; a<listofpages.length; a++){
//going through all the pages of this manuscript to see which one has the correct id so we can input that img
    if (stuff.data[a]['id'] == Page_id){
        var num = a
    }

  }
  console.log(num);
  //console.log(img_keys[3]);
  //console.log(stuff.data[2].file_urls.original);

  for (var i=0; i<img_keys.length; i++) {

     originals_list.push(stuff.data[img_keys[i]].file_urls.original); //this contains a list of all the original image files related to this transcription (from omeka)

  }
  window.originals_list = originals_list;
  console.log(window.originals_list);
  console.log(originals_list); //all the urls for this manuscript
  img = stuff.data[num].file_urls.original; //the img for this page specifically
  img_list[stuff.data.id] = stuff.data[0].element_texts; //????


//from the function above, we can now append the original image of the document to one of the off canvas divs
//$('.original-image-wrapper').append("<div><h3>Original Document</h3><img src = "+img+" /></div>");
//var imgurl = Manuscript_id + "_" + Page_id
//$('.original-image-wrapper').append("<div><h3>Original Document</h3><img src =/static/img/"+imgurl+".jpg></div>");

}
*/


//this is the function that will be run through every time a persName, orgName, placeName a href is clicked in the transcription
// this is the original function
    $("a").click(function(){
      console.log('you clicked on something');
        var href = $(this).attr('href');
        var newhref = href.slice(1, href.length);
        // alert(newhref);
        $.ajax({
            //url: '/static/json/'+newhref+'.json',  //right now, i have made unique jsons with the same id name (they are stored in Django's static/json folder)
            url: '/something/'+newhref,
            type: 'GET',
            dataType: 'json',
            cache: true,
            success: callback_2,
            error: function(data) { console.log("not quite");}

  })


//all the conditions for when someone either clicks a name, or the close button, or another name without closing the first slideout
  function callback_2(data) {
      console.log(data[0]);
      //console.log(data);
      //console.log(data.model);
      //console.log(data.affiliation);
      console.log(newhref);
      //now i need to make these for all the diff models... not just a person

      if (data[0]["model"] == "QI.person") {

        if (data[0]["fields"].birth_date == ""){
          data[0]["fields"].birth_date = 'Unknown'
        }

        if (data[0]["fields"].death_date == ""){
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
        $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Person Information</h3><span> Name </span><p> " + data[0]["fields"].first_name + " " + data[0]["fields"].last_name + "</p><span> Birth Date </span> <p>" + data[0]["fields"].birth_date + "</p> <span> Death Date</span> <p> " + data[0]["fields"].death_date + "</p> <span> Notes </span><p> " + data[0]["fields"].bio_notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].other_names + "</p> <span><a href=/person/"+data[0]["fields"].id_tei +"> &rarr; View more information</a></span><p> </div>");
        $('.off-canvas').animate({"margin-right": '+=25%'});
        $('i.fa.fa-times').animate({"margin-right": '+=25%'});

      }
      else if (newhref == ($('.off-canvas div').attr('id'))) {
          $('.off-canvas').animate({"margin-right": '-=25%'});
          $('i.fa.fa-times').animate({"margin-right": '-=25%'});
          $('.off-canvas div').remove();
      }
       else {
          //this is the case when you click on another (different) a href right after clicking a first one
        $('.off-canvas').animate({"margin-right": '-=25%'});
        $('i.fa.fa-times').animate({"margin-right": '-=25%'});
        $('.off-canvas div').remove();
        $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Person Information</h3><span> Name </span><p> " + data[0]["fields"].first_name + " " + data[0]["fields"].last_name + "</p><span> Birth Date </span> <p>" + data[0]["fields"].birth_date + "</p> <span> Death Date</span> <p> " + data[0]["fields"].death_date + "</p> <span> Notes </span><p> " + data[0]["fields"].bio_notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].other_names + "</p> <span><a href=/person/"+data[0]["fields"].id_tei +"> &rarr; View more information</a></span><p> </div>");
        $('.off-canvas').animate({"margin-right": '+=25%'});
        $('i.fa.fa-times').animate({"margin-right": '+=25%'});

      }
    }
           //end of big if statement !

    else if (data[0]["model"] == "QI.place")  {

      if (data[0]["fields"].county == ""){
        data[0]["fields"].county = 'Unknown';
      }

      if (data[0]["fields"].state == ""){
        data[0]["fields"].state = 'Unknown';
      }

      if (data[0]["fields"].latitude == "") {
        data[0]["fields"].latitude = 'Unknown';
      }

      if (data[0]["fields"].notes == "") {
        data[0]["fields"].notes = 'None';
      }

      if (data[0]["fields"].alternate == "")  {
        data[0]["fields"].alternate = 'None';
      }


    if (($('.off-canvas div').attr('id')) == undefined) {
      $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Place Information</h3><span> Name </span><p> " + data[0]["fields"].name + "</p><span> County </span> <p>" + data[0]["fields"].county + "</p> <span> State </span> <p> " + data[0]["fields"].state + "</p> <span> Location </span> <p>" + data[0]["fields"].latitude + " " + data[0]["fields"].longitude + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].alternate + "</p> <span><a href=/place/"+data[0]["fields"].id_tei +"> &rarr; View more information</a></span><p> </div>");
      $('.off-canvas').animate({"margin-right": '+=25%'});
      $('i.fa.fa-times').animate({"margin-right": '+=25%'});

    }
    else if (newhref == ($('.off-canvas div').attr('id'))) {
        $('.off-canvas').animate({"margin-right": '-=25%'});
        $('i.fa.fa-times').animate({"margin-right": '-=25%'});
        $('.off-canvas div').remove();
    }
     else {
        //this is the case when you click on another (different) a href right after clicking a first one
      $('.off-canvas').animate({"margin-right": '-=25%'});
      $('i.fa.fa-times').animate({"margin-right": '-=25%'});
      $('.off-canvas div').remove();
      $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Place Information</h3><span> Name </span><p> " + data[0]["fields"].name + "</p><span> County </span> <p>" + data[0]["fields"].county + "</p> <span> State </span> <p> " + data[0]["fields"].state + "</p> <span> Location </span> <p>" + data[0]["fields"].latitude + " " + data[0]["fields"].longitude + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].alternate + "</p> <span><a href=/place/"+data[0]["fields"].id_tei +"> &rarr; View more information</a></span><p> </div>");
      $('.off-canvas').animate({"margin-right": '+=25%'});
      $('i.fa.fa-times').animate({"margin-right": '+=25%'});

    }

    }

    else {

      if (data[0]["fields"].date_founded == ""){
        data[0]["fields"].date_founded = 'Unknown';
      }

      if (data[0]["fields"].date_dissolved == ""){
        data[0]["fields"].date_dissolved = 'Unknown';
      }

      if (data[0]["fields"].notes == "") {
        data[0]["fields"].notes = 'Unknown';
      }

      if (data[0]["fields"].associated_spellings == "") {
        data[0]["fields"].associated_spellings = 'None';
      }

      if (data[0]["fields"].other_names == "")  {
        data[0]["fields"].other_names = 'None';
      }

      //start (#1)
    if (($('.off-canvas div').attr('id')) == undefined) {
      $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Organization Information</h3><span> Name </span><p> " + data[0]["fields"].organization_name + "</p><span> Date Founded </span> <p>" + data[0]["fields"].date_founded + "</p> <span> Date Dissolved </span> <p> " + data[0]["fields"].date_dissolved +  "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Associated Spellings </span> <p>" + data[0]["fields"].associated_spellings + "</p> <span> Other Names </span> <p>" + data[0]["fields"].other_names + "</p> <span><a href=/org/"+data[0]["fields"].id_tei +"> &rarr; View more information</a></span><p> </div>");
      $('i.fa.fa-times').animate({"margin-right": '+=25%'});
      $('.off-canvas').animate({"margin-right": '+=25%'});

    }
    else if (newhref == ($('.off-canvas div').attr('id'))) {
        $('.off-canvas').animate({"margin-right": '-=25%'});
        $('i.fa.fa-times').animate({"margin-right": '-=25%'});
        $('.off-canvas div').remove();
    }
     else {
        //this is the case when you click on another (different) a href right after clicking a first one
      $('.off-canvas').animate({"margin-right": '-=25%'});
      $('i.fa.fa-times').animate({"margin-right": '-=25%'});
      $('.off-canvas div').remove();
      $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Organization Information</h3><span> Name </span><p> " + data[0]["fields"].organization_name  + "</p><span> Date Founded </span> <p>" + data[0]["fields"].date_founded + "</p> <span> Date Dissolved </span> <p> " + data[0]["fields"].date_dissolved  + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Associated Spellings </span> <p>" + data[0]["fields"].associated_spellings + "</p> <span> Other Names </span> <p>" + data[0]["fields"].other_names + "</p> <span><a href=/org/"+data[0]["fields"].id_tei +"> &rarr; View more information</a></span><p> </div>");
      $('.off-canvas').animate({"margin-right": '+=25%'});
      $('i.fa.fa-times').animate({"margin-right": '+=25%'});

    }

    }






}

});


//this controls what happens when someone uses the close button

$("i.fa.fa-times").click(function(){
      $('.off-canvas').animate({"margin-right": '-=25%'});
      $('i.fa.fa-times').animate({"margin-right": '-=25%'});
      $('.off-canvas div').remove();


  });
//the below controls how the metadata from off canvas is loaded, and changes the direction of the chevron depending on if you can see the metadata or not
$(".canvas-meta").click(function(){
  if (($('aside.off-canvas-content-meta').attr("id")) == "open") {
    $('.canvas-meta i').css("transform", "rotate(90deg)");
    $('.canvas-meta p').animate({"margin-left": '-=25%'});
    $('aside.off-canvas-content-meta').attr("id", "");
    $('.off-canvas-content-meta').animate({"margin-left": '-=25%'});
  }
  else {

  $('.canvas-meta i').css("transform", "rotate(270deg)");
  $('.canvas-meta p').animate({"margin-left": '+=25%'});
  $('aside.off-canvas-content-meta').attr("id", "open");
  $('.off-canvas-content-meta').animate({"margin-left": '+=25%'});

  }




});
//the below controls how the image from off canvas is loaded, and changes the direction of the chevron depending on if you can see the image or not
$(".canvas-img").click(function(){
  if (($('aside.off-canvas-content-img').attr("id")) == "open") {
    $('.canvas-img i').css("transform", "rotate(90deg)");
    $('.canvas-img p').animate({"margin-left": '-=25%'});
    $('.forwards-arrow i').animate({"margin-left": '-=25%'});
    $('aside.off-canvas-content-img').attr("id", "");
    $('.off-canvas-content-img').animate({"margin-left": '-=25%'});
  }
  else {

  $('.canvas-img i').css("transform", "rotate(270deg)");
  $('.canvas-img p').animate({"margin-left": '+=25%'});
  $('.forwards-arrow i').animate({"margin-left": '+=25%'});
  $('aside.off-canvas-content-img').attr("id", "open");
  $('.off-canvas-content-img').animate({"margin-left": '+=25%'});

  }




});


//controls going forward in the image viewer
$(".forwards-arrow i.fa.fa-chevron-right").click(function(){
  /* var newint = Math.floor(Page_id); // turn page number into an int
  var newint2 = newint+1; // make page number one less
  var newstring = newint2.toString(); // turn new page number into a string
  var newImgUrl = Manuscript_id + "_" + newstring; // this is the new image !!
  window.location.replace('/page/'+newstring+"/#main"); */

// if window.Page_id < lastpage

  if (window.Page_id < lastpage) {
    console.log('nice job');
    window.Page_id = window.Page_id + 1 // increment page number

    if (window.Page_id < 10) {
    var newstring = "00" + window.Page_id.toString(); // turn this into string
  }
  else if (window.Page_id < 100) {
    var newstring = "0" + window.Page_id.toString();
  }
  else {
    var newstring = window.Page_id.toString();
  }

    var newImgUrl = Manuscript_id + "_" + newstring;
    console.log(newImgUrl);
    $('.original-image-wrapper img').remove();
    $('.original-image-wrapper div').append("<img src = /static/img/"+newImgUrl+".png/></div>");
    console.log('got here!!!');

  //  $("body").load("/page/"+newImgUrl); // this lets links work but closes the image tab & just is a problem
 $("#main").load("/page/"+newImgUrl+" #main", function() {
   $.getScript("/static/js/cornplanter2.js");
 }); // this gets the info correctly but disables links
//  $("#main").load("/pageinfo/"+newImgUrl); // does something weird with Image tab but otherwise works
    window.history.pushState("Page Information", "Page Information", "/page/"+newImgUrl+"/");

  //  $("#sidestuff").load("/page/"+newstring+" #sidestuff"); //this makes it closed n not good

  //  window.location.replace('/page/'+newstring);
  }
  else {
    alert('This is the last page of this manuscript!');
  }


/*
  var originals_list = ["https://ds-omeka.haverford.edu/qi/files/original/7da5b5699946e14a1c9e28da828e267e.jpg", "https://ds-omeka.haverford.edu/qi/files/original/3a36c0779b806e6c2c3bc20cbd6c3911.jpg", "https://ds-omeka.haverford.edu/qi/files/original/03d0d21bb2a58d6c560da2a1312cdac5.jpg", "https://ds-omeka.haverford.edu/qi/files/original/8cda22dcaaa62bd99296ead57077ddad.jpg", "https://ds-omeka.haverford.edu/qi/files/original/ce24c92bdd56f563a2a406ecf6e70543.jpg", "https://ds-omeka.haverford.edu/qi/files/original/00bc1a3fbbbf2681cf174eed18601afd.jpg", "https://ds-omeka.haverford.edu/qi/files/original/206798908ef904604b0c435b86f8c039.jpg", "https://ds-omeka.haverford.edu/qi/files/original/d8259bddc835cf80bc6449543ce7aae8.jpg", "https://ds-omeka.haverford.edu/qi/files/original/5c26b923019dce65c0a71c9f34b91336.jpg", "https://ds-omeka.haverford.edu/qi/files/original/3a836e496b7659b6f0dd7e95570ae50e.jpg", "https://ds-omeka.haverford.edu/qi/files/original/70be5c0234db19646d9bbc6ee000e008.jpg", "https://ds-omeka.haverford.edu/qi/files/original/f1257cbc57b23264cbad8218810142f2.jpg", "https://ds-omeka.haverford.edu/qi/files/original/dce309d808dea3f3c1ce2a404f5bf13b.jpg", "https://ds-omeka.haverford.edu/qi/files/original/fe682de239d9daea3dafeecfdc34cf46.jpg", "https://ds-omeka.haverford.edu/qi/files/original/385f773ba59c0215dee131a759124036.jpg", "https://ds-omeka.haverford.edu/qi/files/original/09f0f6d86f38bc5d258e64f9423152ce.jpg", "https://ds-omeka.haverford.edu/qi/files/original/19401c2840ee3006cfb1f4b6c324c34e.jpg", "https://ds-omeka.haverford.edu/qi/files/original/730e79e465cb9e22d99c4d6ae6f6e797.jpg", "https://ds-omeka.haverford.edu/qi/files/original/882fb40b043a44100dc0df5583a126ff.jpg", "https://ds-omeka.haverford.edu/qi/files/original/4bd2f4a79eb454902e0a8786ab1aa9b7.jpg", "https://ds-omeka.haverford.edu/qi/files/original/28fa2049cdd414ffd3bc5ce8e70b6286.jpg", "https://ds-omeka.haverford.edu/qi/files/original/c61fd238cf5a550ccd9ffe5ef224a736.jpg", "https://ds-omeka.haverford.edu/qi/files/original/12c80f22cacdb858eedadd166e7c6683.jpg", "https://ds-omeka.haverford.edu/qi/files/original/019286f87fa9ca169d32f589a74a615b.jpg", "https://ds-omeka.haverford.edu/qi/files/original/41f31de0b45787c6eb3576585e4bdaac.jpg", "https://ds-omeka.haverford.edu/qi/files/original/67369eeefdf676c5a686b2d935136739.jpg", "https://ds-omeka.haverford.edu/qi/files/original/5a36be70279910ffb32dfb27d2c7b1f9.jpg", "https://ds-omeka.haverford.edu/qi/files/original/a208c6d88807a7e39176b3db1447fdb8.jpg", "https://ds-omeka.haverford.edu/qi/files/original/55103ebb238c37ea913f380a2682bf6d.jpg", "https://ds-omeka.haverford.edu/qi/files/original/f4a90dda3e933913eaf4cd1cd1f0424a.jpg", "https://ds-omeka.haverford.edu/qi/files/original/0ffc586a52c8d90ac75de440fdc1627f.jpg", "https://ds-omeka.haverford.edu/qi/files/original/047c25372934bbe2a5090ca07f22cfac.jpg", "https://ds-omeka.haverford.edu/qi/files/original/d0dc1dbbc9ccb7af4b8058871c3e0212.jpg", "https://ds-omeka.haverford.edu/qi/files/original/0da9ea9bb62d9b3a353c40f2c4d60788.jpg", "https://ds-omeka.haverford.edu/qi/files/original/464803961e6e35f2f889c395f8624fba.jpg", "https://ds-omeka.haverford.edu/qi/files/original/a0030ee53b025d1204fd7a00631b6d53.jpg", "https://ds-omeka.haverford.edu/qi/files/original/c09ab9bf30f33a1e90c627e8ef9214b4.jpg", "https://ds-omeka.haverford.edu/qi/files/original/ea55db5c8c5c4b1ba904ee3ffa2a4173.jpg", "https://ds-omeka.haverford.edu/qi/files/original/011cc31f188d8b146411796fc68731b6.jpg", "https://ds-omeka.haverford.edu/qi/files/original/8de7f0be05d39d370f26e808cc447428.jpg", "https://ds-omeka.haverford.edu/qi/files/original/a49eb6426611668a188b91b79ed107f0.jpg", "https://ds-omeka.haverford.edu/qi/files/original/8c2fe72571586c7b0ba1ba7853598133.jpg", "https://ds-omeka.haverford.edu/qi/files/original/c0e3d3367604ef9876b66afb6881533d.jpg", "https://ds-omeka.haverford.edu/qi/files/original/80a737c9963aa2909145dbad4aa385d2.jpg", "https://ds-omeka.haverford.edu/qi/files/original/a8069e0535cfbef164374174f6b50521.jpg", "https://ds-omeka.haverford.edu/qi/files/original/4fe69705bfb74b381072b60bfd4f61d3.jpg", "https://ds-omeka.haverford.edu/qi/files/original/c2b834ba877aa5f6e745745bd302517c.jpg", "https://ds-omeka.haverford.edu/qi/files/original/a67f76186e299939a6ad0a8ff498191e.jpg", "https://ds-omeka.haverford.edu/qi/files/original/08baa3edad6b2f15b2a1a9b0e3e7f669.jpg", "https://ds-omeka.haverford.edu/qi/files/original/e47d785f8e1fe4cfcb1b52032433ebe3.jpg"]
  //the variable above should be brought in differently--like passed in by a function such as get_img()--but I was running out of time and decided to just hard code it

  var currentnum = originals_list.indexOf($('.off-canvas-content-img img').attr('src'))
  var nextnum = currentnum + 1
  console.log(nextnum);
  if (nextnum <= originals_list.length) {
  $('.original-image-wrapper img').remove();
  $('.original-image-wrapper div').append("<img src = "+originals_list[nextnum]+" /></div>");
  var newint = Math.floor(Page_id);
  var newint2 = newint+1;
  var newstring = newint2.toString();
  window.location.replace('/page/'+newstring); // fix this after turning page id into an int
 }
*/
  });

 //controls going backward in the image viewer
$(".forwards-arrow i.fa.fa-chevron-left").click(function(){
/*  var newint = Math.floor(Page_id); // turn page number into an int
  var newint2 = newint-1; // make page number one less
  var newstring = newint2.toString(); // turn new page number into a string
  var newImgUrl = Manuscript_id + "_" + newstring; // this is the new image !!
  window.location.replace('/page/'+newstring+"/#main"); */
  if (window.Page_id > 1) {
    console.log('nice!');
    window.Page_id = window.Page_id - 1 // increment page number

    if (window.Page_id < 10) {
    var newstring = "00" + window.Page_id.toString(); // turn this into string
  }
  else if (window.Page_id < 100) {
    var newstring = "0" + window.Page_id.toString();
  }
  else {
    var newstring = window.Page_id.toString();
  }


    var newImgUrl = Manuscript_id + "_" + newstring;
    $('.original-image-wrapper img').remove();
    $('.original-image-wrapper div').append("<img src = /static/img/"+newImgUrl+".png/></div>");

    $("#main").load("/page/"+newImgUrl+" #main", function() {
      $.getScript("/static/js/cornplanter2.js");
    });

     window.history.pushState("Page Information", "Page Information", "/page/"+newImgUrl+"/");
  //  window.location.replace('/page/'+newstring);
  }
  else {
    alert('This is the first page of this manuscript!');
  }


/*
  var originals_list = ["https://ds-omeka.haverford.edu/qi/files/original/7da5b5699946e14a1c9e28da828e267e.jpg", "https://ds-omeka.haverford.edu/qi/files/original/3a36c0779b806e6c2c3bc20cbd6c3911.jpg", "https://ds-omeka.haverford.edu/qi/files/original/03d0d21bb2a58d6c560da2a1312cdac5.jpg", "https://ds-omeka.haverford.edu/qi/files/original/8cda22dcaaa62bd99296ead57077ddad.jpg", "https://ds-omeka.haverford.edu/qi/files/original/ce24c92bdd56f563a2a406ecf6e70543.jpg", "https://ds-omeka.haverford.edu/qi/files/original/00bc1a3fbbbf2681cf174eed18601afd.jpg", "https://ds-omeka.haverford.edu/qi/files/original/206798908ef904604b0c435b86f8c039.jpg", "https://ds-omeka.haverford.edu/qi/files/original/d8259bddc835cf80bc6449543ce7aae8.jpg", "https://ds-omeka.haverford.edu/qi/files/original/5c26b923019dce65c0a71c9f34b91336.jpg", "https://ds-omeka.haverford.edu/qi/files/original/3a836e496b7659b6f0dd7e95570ae50e.jpg", "https://ds-omeka.haverford.edu/qi/files/original/70be5c0234db19646d9bbc6ee000e008.jpg", "https://ds-omeka.haverford.edu/qi/files/original/f1257cbc57b23264cbad8218810142f2.jpg", "https://ds-omeka.haverford.edu/qi/files/original/dce309d808dea3f3c1ce2a404f5bf13b.jpg", "https://ds-omeka.haverford.edu/qi/files/original/fe682de239d9daea3dafeecfdc34cf46.jpg", "https://ds-omeka.haverford.edu/qi/files/original/385f773ba59c0215dee131a759124036.jpg", "https://ds-omeka.haverford.edu/qi/files/original/09f0f6d86f38bc5d258e64f9423152ce.jpg", "https://ds-omeka.haverford.edu/qi/files/original/19401c2840ee3006cfb1f4b6c324c34e.jpg", "https://ds-omeka.haverford.edu/qi/files/original/730e79e465cb9e22d99c4d6ae6f6e797.jpg", "https://ds-omeka.haverford.edu/qi/files/original/882fb40b043a44100dc0df5583a126ff.jpg", "https://ds-omeka.haverford.edu/qi/files/original/4bd2f4a79eb454902e0a8786ab1aa9b7.jpg", "https://ds-omeka.haverford.edu/qi/files/original/28fa2049cdd414ffd3bc5ce8e70b6286.jpg", "https://ds-omeka.haverford.edu/qi/files/original/c61fd238cf5a550ccd9ffe5ef224a736.jpg", "https://ds-omeka.haverford.edu/qi/files/original/12c80f22cacdb858eedadd166e7c6683.jpg", "https://ds-omeka.haverford.edu/qi/files/original/019286f87fa9ca169d32f589a74a615b.jpg", "https://ds-omeka.haverford.edu/qi/files/original/41f31de0b45787c6eb3576585e4bdaac.jpg", "https://ds-omeka.haverford.edu/qi/files/original/67369eeefdf676c5a686b2d935136739.jpg", "https://ds-omeka.haverford.edu/qi/files/original/5a36be70279910ffb32dfb27d2c7b1f9.jpg", "https://ds-omeka.haverford.edu/qi/files/original/a208c6d88807a7e39176b3db1447fdb8.jpg", "https://ds-omeka.haverford.edu/qi/files/original/55103ebb238c37ea913f380a2682bf6d.jpg", "https://ds-omeka.haverford.edu/qi/files/original/f4a90dda3e933913eaf4cd1cd1f0424a.jpg", "https://ds-omeka.haverford.edu/qi/files/original/0ffc586a52c8d90ac75de440fdc1627f.jpg", "https://ds-omeka.haverford.edu/qi/files/original/047c25372934bbe2a5090ca07f22cfac.jpg", "https://ds-omeka.haverford.edu/qi/files/original/d0dc1dbbc9ccb7af4b8058871c3e0212.jpg", "https://ds-omeka.haverford.edu/qi/files/original/0da9ea9bb62d9b3a353c40f2c4d60788.jpg", "https://ds-omeka.haverford.edu/qi/files/original/464803961e6e35f2f889c395f8624fba.jpg", "https://ds-omeka.haverford.edu/qi/files/original/a0030ee53b025d1204fd7a00631b6d53.jpg", "https://ds-omeka.haverford.edu/qi/files/original/c09ab9bf30f33a1e90c627e8ef9214b4.jpg", "https://ds-omeka.haverford.edu/qi/files/original/ea55db5c8c5c4b1ba904ee3ffa2a4173.jpg", "https://ds-omeka.haverford.edu/qi/files/original/011cc31f188d8b146411796fc68731b6.jpg", "https://ds-omeka.haverford.edu/qi/files/original/8de7f0be05d39d370f26e808cc447428.jpg", "https://ds-omeka.haverford.edu/qi/files/original/a49eb6426611668a188b91b79ed107f0.jpg", "https://ds-omeka.haverford.edu/qi/files/original/8c2fe72571586c7b0ba1ba7853598133.jpg", "https://ds-omeka.haverford.edu/qi/files/original/c0e3d3367604ef9876b66afb6881533d.jpg", "https://ds-omeka.haverford.edu/qi/files/original/80a737c9963aa2909145dbad4aa385d2.jpg", "https://ds-omeka.haverford.edu/qi/files/original/a8069e0535cfbef164374174f6b50521.jpg", "https://ds-omeka.haverford.edu/qi/files/original/4fe69705bfb74b381072b60bfd4f61d3.jpg", "https://ds-omeka.haverford.edu/qi/files/original/c2b834ba877aa5f6e745745bd302517c.jpg", "https://ds-omeka.haverford.edu/qi/files/original/a67f76186e299939a6ad0a8ff498191e.jpg", "https://ds-omeka.haverford.edu/qi/files/original/08baa3edad6b2f15b2a1a9b0e3e7f669.jpg", "https://ds-omeka.haverford.edu/qi/files/original/e47d785f8e1fe4cfcb1b52032433ebe3.jpg"]
  //the variable above should be brought in differently--like passed in by a function such as get_img()--but I was running out of time and decided to just hard code it

  var currentnum = originals_list.indexOf($('.off-canvas-content-img img').attr('src'))

  var nextnum = currentnum - 1
  console.log(nextnum);
  if (nextnum >= 0) { //make sure we dont get into a negative index
      $('.original-image-wrapper img').remove();
      $('.original-image-wrapper div').append("<img src = "+originals_list[nextnum]+" /></div>");

  }

*/

  });












});

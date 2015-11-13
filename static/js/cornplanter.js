$(document).ready(function() {
  console.log('Got here');
  // this is just to check the script is working


// now we are going to immediately load the metadata and image 
//information of the transcription we are viewing into the off canvas divs to the left (meta/img)
$.ajax({
                  url: 'https://ds-omeka.haverford.edu/qi/api/items/2635',
                  type: 'GET',
                  dataType: 'jsonp',
                  cache: true,
                  success: callback_3,  //call a function to get all metadata in order, get information from omeka
                  error: function(data) { console.log("not quite");}
                })

function callback_3(data) {

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
  $(".off-canvas-content-meta").append("<div><h3>Metadata</h3><span class='meta-title'> Name of Document </span> <p>" + my_dict["Title"] + "</p> <span class='meta-title'> Creator </span><p> " + my_dict["Creator"] + "</p><span class='meta-title'> Date </span><p> " + my_dict["Date"] + "</p> <span class='meta-title'> Type of Document </span> <p>" + my_dict["Material Type"] + "</p><span class='meta-title'> Call Number </span><p> " + my_dict["Call Number"] + "</p></div>");


// next, we get the actual image of the document from omeka from the variable I created above, called url_thing
$.ajax({
    url: url_thing,
    type: 'GET',
    dataType: 'jsonp',
    cache: true,
    success: get_img, //call a function to get image information
    error: function(stuff) { console.log("not quite 2");}
  })



}

function get_img(stuff) {

  var img_list = {}
  var img = {}

  img = stuff.data[0].file_urls.original;
  img_list[stuff.data.id] = stuff.data[0].element_texts;

//from the function above, we can now append the original image of the document to one of the off canvas divs
$('.off-canvas-content-img').append("<div><h3>Original Document</h3><img src = "+img+" /></div>");



}

  
//this is the function that will be run through every time a persName, orgName, placeName a href is clicked in the transcription
  $("a").click(function(){
        var href = $(this).attr('href');
        var newhref = href.slice(1, href.length);
        // alert(newhref);
        $.ajax({
            url: '/static/json/'+newhref+'.json',  //right now, i have made unique jsons with the same id name (they are stored in Django's static/json folder)
            type: 'GET',
            dataType: 'json',
            cache: true,
            success: callback_2,
            error: function(data) { console.log("not quite");}

  })

        


  
//all the conditions for when someone either clicks a name, or the close button, or another name without closing the first slideout
  function callback_2(data) {
      console.log(data.name);
      console.log(data.affiliation);
      console.log(newhref);

      if (($('.off-canvas div').attr('id')) == undefined) {
        $('.off-canvas').append("<div id = "+newhref+"><h3>Person Information</h3><span> Name </span><p> " + data.name + "</p><span> Birth </span> <p>" + data.birth + "</p> <span> Death </span> <p> " + data.death + "</p> <span> Affiliation </span> <p>" + data.affiliation + "</p> <span> Notes </span><p> " + data.notes + "</p> <span> Alternate Spellings </span> <p>" + data.associated_spellings + "</p> <span> Other Documents </span><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span> <p><a href =" + data.library_of_congress_info + ">"+data.library_of_congress_info+"</a></p></div>");
        $('.off-canvas').animate({"margin-right": '+=25%'});
        $('i.fa.fa-times').animate({"margin-right": '+=25%'});

      }
      else if (newhref == ($('.off-canvas div').attr('id'))) {
          $('.off-canvas').animate({"margin-right": '-=25%'});
          $('i.fa.fa-times').animate({"margin-right": '-=25%'});
          $('.off-canvas div').remove();
      }
       else { //this is the case when you click on another (different) a href right after clicking a first one
        $('.off-canvas').animate({"margin-right": '-=25%'});
        $('i.fa.fa-times').animate({"margin-right": '-=25%'});
        $('.off-canvas div').remove();
        $('.off-canvas').append("<div id = "+newhref+"><h3>Person Information</h3><span> Name </span><p> " + data.name + "</p><span> Birth </span> <p>" + data.birth + "</p> <span> Death </span> <p> " + data.death + "</p> <span> Affiliation </span> <p>" + data.affiliation + "</p> <span> Notes </span><p> " + data.notes + "</p> <span> Alternate Spellings </span> <p>" + data.associated_spellings + "</p> <span> Other Documents </span><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span> <p><a href =" + data.library_of_congress_info + ">"+data.library_of_congress_info+"</a></p></div>");
        $('.off-canvas').animate({"margin-right": '+=25%'});
        $('i.fa.fa-times').animate({"margin-right": '+=25%'});
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
    $('aside.off-canvas-content-img').attr("id", "");
    $('.off-canvas-content-img').animate({"margin-left": '-=25%'});
  }
  else {

  $('.canvas-img i').css("transform", "rotate(270deg)");
  $('.canvas-img p').animate({"margin-left": '+=25%'});
  $('aside.off-canvas-content-img').attr("id", "open");
  $('.off-canvas-content-img').animate({"margin-left": '+=25%'});

  }
 



});


     

 
  
  	
  



});

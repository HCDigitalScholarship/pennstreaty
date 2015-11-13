$(document).ready(function() {
  // console.log('Got here');

// grabs metadata info including pdf
  // var metadata_list = {}
  // var trans_list = {}
  $.ajax({
	  url: 'https://ds-omeka.haverford.edu/qi/api/items/4893',
	  type: 'GET',
	  dataType: 'jsonp',
	  cache: true,
	  success: callback_2,
	  error: function(data) { console.log("not quite");}
  })

  function callback_2(data) {
    // console.log(data.data.files.url);
     // console.log(data.data.element_texts);

      var metadata_list = {}
      var url_thing = {}
      url_thing = data.data.files.url;
      metadata_list[data.data.id] = data.data.element_texts;
      // console.log(metadata_list[data.data.id]);
     
  	 
  	 
  		 //    metadata_list[data.data.id] = data.data.element_texts;
     //      trans_list[data.data.id] = data.data.files; //url that brings you to all transcriptions for that certain object
         
  	  // }
  	 
     //  console.log(metadata_list[data.data[0].id]);
     //  console.log(trans_list[data.data[1].id]);


 

  	
  	meta_keys = Object.keys(metadata_list);
   //  console.log(meta_keys); //id number
  	// console.log(metadata_list[meta_keys[0]][0].text);
  	for (var i=0; i<meta_keys.length; i++) {
  	  my_dict = {}
  	  for (var j=0; j<metadata_list[meta_keys[i]].length; j++) {
  		  var type = metadata_list[meta_keys[i]][j].element.name;
        // console.log(type);
  		  var content = metadata_list[meta_keys[i]][j].text;
  		  my_dict[type] = content;
  	  }
        
  	}
  console.log(my_dict["Creator"]);
  $("#metastuffdata").append("<div><span class='meta-title'> Name of Document </span> <p>" + my_dict["Title"] + "</p> <span class='meta-title'> Creator </span><p> " + my_dict["Creator"] + "</p><span class='meta-title'> Date </span><p> " + my_dict["Date"] + "</p> <span class='meta-title'> Type of Document </span> <p>" + my_dict["Material Type"] + "</p><span class='meta-title'> Call Number </span><p> " + my_dict["Call Number"] + "</p></div>");
  

$.ajax({
    url: url_thing,
    type: 'GET',
    dataType: 'jsonp',
    cache: true,
    success: get_trans,
    error: function(stuff) { console.log("not quite 2");}
  })


  
}

function get_trans(stuff) {
  // console.log(stuff.data);
  var img_list = {}
  var img = {}
  var transcription = {}
  
  // console.log(stuff.data[0].file_urls.original);
  // console.log(stuff.data[0].element_texts);

  img = stuff.data[0].file_urls.original;
  img_list[stuff.data.id] = stuff.data[0].element_texts;

  trans_keys = Object.keys(img_list);
    
    //console.log(img_list[trans_keys[0]][0].text);
    for (var i=0; i<trans_keys.length; i++) {
      my_dict = {}
      for (var j=0; j<img_list[trans_keys[i]].length; j++) {
        var type = img_list[trans_keys[i]][j].element.name;
        var content = img_list[trans_keys[i]][j].text;
        my_dict[type] = content;
      }
        
    }

 console.log(my_dict["Transcription"]);
 transcription = my_dict["Transcription"];
 console.log("-----------------------");
 console.log(transcription);
 console.log(img);


$('div #transimg').append("<img src = "+img+" />");
$('div #transcription').append("<p>"+transcription+"</p>");


}

});

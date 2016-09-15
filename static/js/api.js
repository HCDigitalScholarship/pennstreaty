// // Javascript for transcriptions and texts page.
// helpful place to start:
// list of all items: https://ds-omeka.haverford.edu/qi/api/items
// list of one item: https://ds-omeka.haverford.edu/qi/api/items/4919
// list of the transcriptions the item is connected to: https://ds-omeka.haverford.edu/qi/api/files?item=4919

$(document).ready(function() {
  // console.log('Got here');

// grabs metadata info including pdf
  var metadata_list = {}
  var trans_list = {}
  var id_list = {}
  $.ajax({
	  url: 'https://ds-omeka.haverford.edu/qi/api/items',
	  type: 'GET',
	  dataType: 'jsonp',
	  cache: true,
	  success: callback_2,
	  error: function(data) { console.log("not quite");}
  })

  function callback_2(data) {
     // console.log(data.data);
      // console.log(data.data[0].element_texts);
      // console.log(data.data[0].id);
  	 for (var i=0; i<data.data.length; i++) {
  	  if (data.data[i].element_texts) {
          id_list[data.data[i].id] = data.data[i].id;
  		    metadata_list[data.data[i].id] = data.data[i].element_texts;
          trans_list[data.data[i].id] = data.data[i].files; //url that brings you to all transcriptions for that certain object
         
  	  }
  	 }
      console.log(id_list);
      console.log(metadata_list);
      // console.log(trans_list[data.data[1].id]);


 

  	id_keys = Object.keys(id_list);
  	meta_keys = Object.keys(metadata_list);
    // console.log(id_list[id_keys[2]]);
  	// console.log(metadata_list[meta_keys[2]]);
  	for (var i=0; i<meta_keys.length; i++) {
  	  my_dict = {}
      my_id = {}
  	  for (var j=0; j<metadata_list[meta_keys[i]].length; j++) {
  		  var type = metadata_list[meta_keys[i]][j].element.name;
  		  var content = metadata_list[meta_keys[i]][j].text;
        // console.log(content);
  		  my_dict[type] = content;
       
  	  }
      my_dict["id"] = data.data[i].id; //each has unique id

    $("table.display").dataTable().fnDestroy();
    $('table.display tbody').append("<tr><td><a href='"+my_dict["id"]+"' class='man-list'>"+my_dict["Title"]+"</a></td><td>"+my_dict["Creator"]+"</td><td>"+my_dict["Date"]+"</td><td>"+my_dict["Material Type"]+"</td><td>"+my_dict["Call Number"]+"</td></tr>");
      $('table.display').DataTable( {
          "aLengthMenu": [[25, 50, -1], [25, 50, "All"]]

    } );

      }

      $(".man-list").each(function(index, value) {
         
                var href = ($(this).attr('href'));
                if (href != "2635") {
                  console.log ("lol");
                }
                else {
                $.ajax({
                  url: 'https://ds-omeka.haverford.edu/qi/api/items/' + href,
                  type: 'GET',
                  dataType: 'jsonp',
                  cache: true,
                  success: callback_3,
                  error: function(data) { console.log("not quite");}
                })

                function callback_3(data) {
                    // console.log(data.data.files.url);

                    var metadata_list = {}
                    var url_thing = {}
                    url_thing = data.data.files.url;
                    metadata_list[data.data.id] = data.data.element_texts;

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
          var meta = ""
         
          meta += "<p> <span class='meta-title'> Name of Document </span> " + my_dict["Title"] + "</p><p> <span class='meta-title'> Creator </span> " + my_dict["Creator"] + "</p><p> <span class='meta-title'> Date </span> " + my_dict["Date"] + "</p><p> <span class='meta-title'> Type of Document </span> " + my_dict["Material Type"] + "</p><p> <span class='meta-title'> Call Number </span> " + my_dict["Call Number"] + "</p>";
        
    }
          

    $.ajax({
    url: url_thing,
    type: 'GET',
    dataType: 'jsonp',
    cache: true,
    success: get_trans,
    error: function(stuff) { console.log("not quite 2");}
  })

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
    
      // transcription = my_dict["Transcription"];
      // if (transcription="undefined") {
      //   transcription = "";
      // }
 // console.log(my_dict["Transcription"]);
 // transcription = my_dict["Transcription"];
 // console.log("-----------------------");
 // console.log(transcription);
 // console.log(img);


  $('#metadatatrans #imgmeta').append("<div style='display: none;'><img src = "+img+" /></div>");
  $('#metadatatrans #metastuff').append("<div style='display: none;'>"+meta+"</div>");
  $('#metadatatrans #trans').append("<div style='display: none;'><p>"+transcription+"</p></div>");


}




  }

     }         
          
      });

     

   }
  
  



});



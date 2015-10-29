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
  	 for (var i=0; i<data.data.length; i++) {
  	  if (data.data[i].element_texts) {
  		    metadata_list[data.data[i].id] = data.data[i].element_texts;
          trans_list[data.data[i].id] = data.data[i].files; //url that brings you to all transcriptions for that certain object
         
  	  }
  	 }
      // console.log(metadata_list[data.data[0].id]);
      // console.log(trans_list[data.data[1].id]);


 

  	//creates each link in manuscript list
  	var script_list = $(".dropdown-menu.all-man")
  	var script_list_holder = $(".handwritten .row")
  	meta_keys = Object.keys(metadata_list);
  	// console.log(metadata_list[meta_keys[0]][12].text);
  	for (var i=0; i<meta_keys.length; i++) {
  	  my_dict = {}
  	  for (var j=0; j<metadata_list[meta_keys[i]].length; j++) {
  		  var type = metadata_list[meta_keys[i]][j].element.name;
  		  var content = metadata_list[meta_keys[i]][j].text;
        // console.log(content);
  		  my_dict[type] = content;
  	  }
      

    $('table.display tbody').append("<tr><td>"+my_dict["Title"]+"</td><td>"+my_dict["Creator"]+"</td><td>"+my_dict["Date"]+"</td><td>"+my_dict["Material Type"]+"</td><td>"+my_dict["Call Number"]+"</td></tr>");

    

}

$('table.display').DataTable( {
   "aLengthMenu": [[25, 50, -1], [25, 50, "All"]]

    } );


  	}
  	
  


});

$(document).ready(function() {
  console.log('Got here');
  

  $("a").click(function(){
        var href = $(this).attr('href');
        var newhref = href.slice(1, href.length);
        alert(newhref);
        $.ajax({
            url: '/'+newhref+'',
            type: 'GET',
            dataType: 'json',
            cache: true,
            success: callback_2,
            error: function(data) { console.log("not quite");}

  })

        
});

  

  function callback_2(data) {
      console.log(data.name);
      console.log(data.affiliation);

      $('.slider').append("<div><span> Name </span><hr><p> " + data.name + "</p><span> Birth </span> <hr><p>" + data.birth + "</p> <span> Death </span> <hr><p> " + data.death + "</p> <span> Affiliation </span><hr> <p>" + data.affiliation + "</p> <span> Notes </span><hr><p> " + data.notes + "</p> <span> Alternate Spellings </span> <hr><p>" + data.associated_spellings + "</p> <span> Other Documents </span><hr><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span><hr> <p>" + data.library_of_congress_info + "</p></div>");

      $('.slider').animate({"margin-right": '+=200'});
      $('#transcription').animate({"margin-right": '+=200'});


 


//       // console.log(data.data[0].element_texts);
//       console.log(data.data[0].id);
//   	//  for (var i=0; i<data.data.length; i++) {
//   	//   if (data.data[i].element_texts) {
//    //        id_list[data.data[i].id] = data.data[i].id;
//   	// 	    metadata_list[data.data[i].id] = data.data[i].element_texts;
//    //        trans_list[data.data[i].id] = data.data[i].files; //url that brings you to all transcriptions for that certain object
         
//   	//   }
//   	//  }
//    //    console.log(id_list);
//    //    console.log(metadata_list);
//    //    // console.log(trans_list[data.data[1].id]);


 

//   	// id_keys = Object.keys(id_list);
//   	// meta_keys = Object.keys(metadata_list);
//    //  // console.log(id_list[id_keys[2]]);
//   	// // console.log(metadata_list[meta_keys[2]]);
//   	// for (var i=0; i<meta_keys.length; i++) {
//   	//   my_dict = {}
//    //    my_id = {}
//   	//   for (var j=0; j<metadata_list[meta_keys[i]].length; j++) {
//   	// 	  var type = metadata_list[meta_keys[i]][j].element.name;
//   	// 	  var content = metadata_list[meta_keys[i]][j].text;
//    //      // console.log(content);
//   	// 	  my_dict[type] = content;
       
//   	//   }
//    //    my_dict["id"] = data.data[i].id; //each has unique id

   

      }


     

 
  
  	
  



});

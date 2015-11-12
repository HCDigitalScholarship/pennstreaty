$(document).ready(function() {
  console.log('Got here');
  

  $("a").click(function(){
        var href = $(this).attr('href');
        var newhref = href.slice(1, href.length);
        // alert(newhref);
        $.ajax({
            url: '/static/json/'+newhref+'.json',
            type: 'GET',
            dataType: 'json',
            cache: true,
            success: callback_2,
            error: function(data) { console.log("not quite");}

  })

        


  

  function callback_2(data) {
      console.log(data.name);
      console.log(data.affiliation);
      console.log(newhref);

      if (($('.off-canvas div').attr('id')) == undefined) {
        $('.off-canvas').append("<div id = "+newhref+"><span> Name </span><p> " + data.name + "</p><span> Birth </span> <p>" + data.birth + "</p> <span> Death </span> <p> " + data.death + "</p> <span> Affiliation </span> <p>" + data.affiliation + "</p> <span> Notes </span><p> " + data.notes + "</p> <span> Alternate Spellings </span> <p>" + data.associated_spellings + "</p> <span> Other Documents </span><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span> <p><a href =" + data.library_of_congress_info + ">"+data.library_of_congress_info+"</a></p></div>");
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
        $('.off-canvas').append("<div id = "+newhref+"><span> Name </span><p> " + data.name + "</p><span> Birth </span> <p>" + data.birth + "</p> <span> Death </span> <p> " + data.death + "</p> <span> Affiliation </span> <p>" + data.affiliation + "</p> <span> Notes </span><p> " + data.notes + "</p> <span> Alternate Spellings </span> <p>" + data.associated_spellings + "</p> <span> Other Documents </span><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span> <p><a href =" + data.library_of_congress_info + ">"+data.library_of_congress_info+"</a></p></div>");
        $('.off-canvas').animate({"margin-right": '+=25%'});
        $('i.fa.fa-times').animate({"margin-right": '+=25%'});
      }
      
        
      
   
    


}

});



$("i.fa.fa-times").click(function(){
      $('.off-canvas').animate({"margin-right": '-=25%'});
      $('i.fa.fa-times').animate({"margin-right": '-=25%'});
      $('.off-canvas div').remove();
      



  });


     

 
  
  	
  



});

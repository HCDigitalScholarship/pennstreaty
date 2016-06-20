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

    //start (#1)
  if (($('.off-canvas div').attr('id')) == undefined) {
    console.log("its happening");
    $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Person Information</h3><span> Name </span><p> " + data[0]["fields"].first_name + " " + data[0]["fields"].last_name + "</p><span> Birth </span> <p>" + data[0]["fields"].birth_date + "</p> <span> Death </span> <p> " + data[0]["fields"].death_date + "</p> <span> Affiliation </span> <p>" + data[0]["fields"].affiliations + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].other_names + "</p> <span> Other Documents </span><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span> <p><a href =" + data.library_of_congress_info + ">"+data.library_of_congress_info+"</a></p></div>");
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
    $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Person Information</h3><span> Name </span><p> " + data[0]["fields"].first_name + " " + data[0]["fields"].last_name + "</p><span> Birth </span> <p>" + data[0]["fields"].birth_date + "</p> <span> Death </span> <p> " + data[0]["fields"].death_date + "</p> <span> Affiliation </span> <p>" + data[0]["fields"].affiliations + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].other_names  + "</p> <span> Other Documents </span><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span> <p><a href =" + data.library_of_congress_info + ">"+data.library_of_congress_info+"</a></p></div>");
    $('.off-canvas').animate({"margin-right": '+=25%'});
    $('i.fa.fa-times').animate({"margin-right": '+=25%'});

  }
}
       //end of big if statement !

else if (data[0]["model"] == "QI.place")  {

if (($('.off-canvas div').attr('id')) == undefined) {
  $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Place Information</h3><span> Name </span><p> " + data[0]["fields"].name + "</p><span> County </span> <p>" + data[0]["fields"].county + "</p> <span> State </span> <p> " + data[0]["fields"].state + "</p> <span> Location </span> <p>" + data[0]["fields"].latitude + " " + data[0]["fields"].longitude + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].alternate + "</p> <span> Other Documents </span><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span> <p><a href =" + data.library_of_congress_info + ">"+data.library_of_congress_info+"</a></p></div>");
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
  $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Person Information</h3><span> Name </span><p> " + data[0]["fields"].name + "</p><span> County </span> <p>" + data[0]["fields"].county + "</p> <span> State </span> <p> " + data[0]["fields"].state + "</p> <span> Location </span> <p>" + data[0]["fields"].latitude + " " + data[0]["fields"].longitude + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Alternate Spellings </span> <p>" + data[0]["fields"].alternate  + "</p> <span> Other Documents </span><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span> <p><a href =" + data.library_of_congress_info + ">"+data.library_of_congress_info+"</a></p></div>");
  $('.off-canvas').animate({"margin-right": '+=25%'});
  $('i.fa.fa-times').animate({"margin-right": '+=25%'});

}

}

else {

  //start (#1)
if (($('.off-canvas div').attr('id')) == undefined) {
  $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Organization Information</h3><span> Name </span><p> " + data[0]["fields"].organization_name + "</p><span> Date Founded </span> <p>" + data[0]["fields"].date_founded + "</p> <span> Date Dissolved </span> <p> " + data[0]["fields"].date_dissolved +  "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Associated Spellings </span> <p>" + data[0]["fields"].associated_spellings + "</p> <span> Other Names </span> <p>" + data[0]["fields"].other_names + "</p> <span> Other Documents </span><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span> <p><a href =" + data.library_of_congress_info + ">"+data.library_of_congress_info+"</a></p></div>");
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
  $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Organization Information</h3><span> Name </span><p> " + data[0]["fields"].organization_name  + "</p><span> Date Founded </span> <p>" + data[0]["fields"].date_founded + "</p> <span> Date Dissolved </span> <p> " + data[0]["fields"].date_dissolved  + "</p> <span> Notes </span><p> " + data[0]["fields"].notes + "</p> <span> Associated Spellings </span> <p>" + data[0]["fields"].associated_spellings + "</p> <span> Other Names </span> <p>" + data[0]["fields"].other_names + "</p> <span> Other Documents </span><p> " + data.other_docs_assoc + "</p><span> Library of Congress Information </span> <p><a href =" + data.library_of_congress_info + ">"+data.library_of_congress_info+"</a></p></div>");
  $('.off-canvas').animate({"margin-right": '+=25%'});
  $('i.fa.fa-times').animate({"margin-right": '+=25%'});

}

}






}

});

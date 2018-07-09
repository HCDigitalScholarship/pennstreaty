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

     if (($('.popoverInfo div').attr('id')) == undefined) {
      console.log("its happening!");
      $('.popover-body').append("<span> Name </span><p> " + data[0]["fields"].first_name + " " + data[0]["fields"].last_name + "</p><span> Birth Date </span> <p>" + data[0$

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
    else {
      data[0]["fields"].latitude = data[0]["fields"].latitude + " N"
      data[0]["fields"].longitude = data[0]["fields"].longitude + " W"
    }

    if (data[0]["fields"].notes == "") {
      data[0]["fields"].notes = 'None';
    }

    if (data[0]["fields"].alternate == "")  {
      data[0]["fields"].alternate = 'None';
    }


  if (($('.off-canvas div').attr('id')) == undefined) {
    $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Place Information</h3><span> Name </span><p> " + data[0]["fields"].name + "</p><span> County </span> <p>" + da$
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
    $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Place Information</h3><span> Name </span><p> " + data[0]["fields"].name + "</p><span> County </span> <p>" + da$
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
    $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Organization Information</h3><span> Name </span><p> " + data[0]["fields"].organization_name + "</p><span> Date$
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
    $('.off-canvas').append("<div id = "+newhref+"><br /><h3>Organization Information</h3><span> Name </span><p> " + data[0]["fields"].organization_name  + "</p><span> Dat$
    $('.off-canvas').animate({"margin-right": '+=25%'});
    $('i.fa.fa-times').animate({"margin-right": '+=25%'});

  }

  }






}

});


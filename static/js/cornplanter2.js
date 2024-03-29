$(document).ready(function(){
$("a").one('click',function(){
    console.log('you clicked on something');
    var href = $(this).attr('href');
    var newhref = href.slice(1, href.length);
    var popover_id=$(this).attr('id');
    var toggle_id=$(this).attr('data-toggle');
//    console.log(popover_id);
//    console.log(toggle_id);
   // alert(newhref);
    $.ajax({
        //url: '/static/json/'+newhref+'.json',  //right now, i have made unique jsons with the same id name (they are stored in Django's static/json folder)
        url: '/something/'+newhref,
        type: 'GET',
        dataType: 'json',
        cache: true,
        success: callback_2,
        error: function(data) { console.log("not quite");},
       });

//all the conditions for when someone either clicks a name, or the close button, or another name without closing the first slideout
function callback_2(data){
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

       var popoverbody_id="Per-popover-body-"+popover_id.slice(12);
    // console.log(popoverbody_id);
       var information = "<div> Name: " + data[0]["fields"].first_name + " " + data[0]["fields"].last_name + "</div><div> Birth Date: " + data[0]["fields"].birth_date + "</div> <div> Death Date: " + data[0]["fields"].death_date + "</div> <div> Notes: " + data[0]["fields"].bio_notes.substr(0,120) + "...</div> <div><a href=/person/"+data[0]["fields"].id_tei +"> &rarr; View more information</a><div>";
       var target_to_toggle='[data-toggle='+toggle_id+']';
//     console.log(information);
//     console.log(target_to_toggle);
      $('#'+popoverbody_id).append(information);

       $(target_to_toggle).popover({
         html: true,
         content: function() {
         var content = $(this).attr("data-popover-content");
         return $(content).children("#"+popoverbody_id).html();
        },
         title: function() {
         var title = $(this).attr("data-popover-content");
         return $(title).children("#Per-popover-header").html();
        }

      });



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

       var popoverbody_id="Pla-popover-body-"+popover_id.slice(12);
       //console.log(popoverbody_id);
       var target_to_toggle='[data-toggle='+toggle_id+']';
       var information = "<div> Name: " + data[0]["fields"].name + "</div><div> County: " + data[0]["fields"].county + "</div> <div> State: " + data[0]["fields"].state + "</div> <div> Location: " + data[0]["fields"].latitude + " " + data[0]["fields"].longitude + "</div> <div> Notes: " + data[0]["fields"].notes.substr(0,120) + "</div> <div> Alternate Spellings: "+ data[0]["fields"].alternate + "</div> <div><a href=/place/"+data[0]["fields"].id_tei +"> &rarr; View more information</a></div>"

       $('#'+popoverbody_id).append(information);  


       $( target_to_toggle).popover({
         html: true,
         content: function() {
         var content = $(this).attr("data-popover-content");
         return $(content).children("#"+popoverbody_id).html();
        },
         title: function() {
         var title = $(this).attr("data-popover-content");
         return $(title).children("#Pla-popover-header").html();
        }
      });
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

       var popoverbody_id="Org-popover-body-"+popover_id.slice(12);
       //console.log(popoverbody_id);
       var target_to_toggle='[data-toggle='+toggle_id+']';
       var information = "<div>Name: " + data[0]["fields"].organization_name + "</div><div> Date Founded: " + data[0]["fields"].date_founded + "</div><div> Date Disssolved: " + data[0]["fields"].date_dissolved +  "</div> <div> Notes: " + data[0]["fields"].notes.substr(0,120) + "...</div> <div> Associated Spellings: " + data[0]["fields"].associated_spellings + "</div><div> Other Names: " + data[0]["fields"].other_names + "</div><div><a href=/org/"+data[0]["fields"].id_tei +"> &rarr; View more information</a></div>"
       $('#'+ popoverbody_id).append(information);
        
        $(target_to_toggle).popover({
         html: true,
         content: function() {
         var content = $(this).attr("data-popover-content");
         return $(content).children('#'+popoverbody_id).html();
        },
         title: function() {
         var title = $(this).attr("data-popover-content");
         return $(title).children('#Org-popover-header').html();
        }
      });


}

}        



/*$(document).ready(function(){
$("a").one('click',function(){
    console.log('you clicked on something');
    var href = $(this).attr('href');
    var newhref = href.slice(1, href.length);
    var popover_id=$(this).attr('id');
    var toggle_id=$(this).attr('data-toggle');
//    console.log(popover_id);
//    console.log(toggle_id);
   // alert(newhref);
    $.ajax({
        //url: '/static/json/'+newhref+'.json',  //right now, i have made unique jsons with the same id name (they are stored in Django's static/json folder)
        url: '/something/'+newhref,
        type: 'GET',
        dataType: 'json',
        cache: true,
        success: callback_2,
        error: function(data) { console.log("not quite");},
       });*/

});
})

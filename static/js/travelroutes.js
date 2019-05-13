class Main
  constructor: ->
    @pickHangers()

  pickHangers: ->
    $('ul[class*=-block-grid-').each (i, el) =>
      # define elements
      $ul = $(el)
      # we reverse this now to use later
      $lis = $ul.find('li')

      # string matching to get row count
      str = $ul.attr('class')
      re = /\w+\-block\-grid\-(\d+)\b/i
      rowCount = str.match(re)[1]

      # finding total length and remainders
      length = $lis.length
      remainder = length % rowCount

      #
      if (remainder > 0)
        $liLastRow = $($lis.slice(-remainder))

        multiplier = rowCount - remainder
        width = @getWidthPercentage($lis, multiplier)
        $liLastRow.first().css("margin-left": "#{width}%")

  getWidthPercentage: ($el, n) ->
    width = $el.outerWidth()*n
    parentWidth = $el.parent().outerWidth()
    percent = 100*(width/parentWidth)/2
        
$(-> main = new Main())
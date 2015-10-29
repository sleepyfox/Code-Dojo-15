# InventoryManager
ItemFactorySingleton = (n, sb , q) ->
  @n = n
  @sb = sb
  @q = q
i = [] # List of items
i.push new ItemFactorySingleton("+5 Dexterity Vest", 10, 20) # Great for Rouges
i.push new ItemFactorySingleton("Aged Brie", 2, 0) # Stinky
i.push new ItemFactorySingleton("Elixir of the Mongoose", 5, 7) # Mongoose vs. Cobra: FIGHT!
i.push new ItemFactorySingleton("Sulfuras, Hand of Ragnaros", 0, 80) # Legendary
i.push new ItemFactorySingleton("Backstage passes to a TAFKAL80ETC concert", 15, 20) # The Artist Formerly Known As Level 80 Tauren Chieftains
i.push new ItemFactorySingleton("Conjured Mana Cake", 3, 6) # TODO: add conjured item logic to update quality function
exports.i = i
update_quality = (i) ->
  j = 0 # because I'd already used i, dammit
  while j < i.length - 1
    if i[j].n != "Aged Brie" and i[j].n != "Backstage passes to a TAFKAL80ETC concert"
      if i[j].q > 0
        if i[j].n != "Sulfuras, Hand of Ragnaros"
          i[j].q = i[j].q - 1  # Because Sulfuras is Legendary
    else
      if i[j].q < 50
        i[j].q = i[j].q + 1
        # 
        # Backstage passes logic
        #
        if i[j].n == "Backstage passes to a TAFKAL80ETC concert"
          if i[j].sb < 11
            if i[j].q < 50  
              i[j].q = i[j].q + 1  
          if i[j].sb < 6
            if i[j].q < 50  
              i[j].q = i[j].q + 1 
    #
    # Legendary item logic
    #
    if i[j].n != "Sulfuras, Hand of Ragnaros"
      i[j].sb = i[j].
      sb - 1  
    if i[j].sb < 0
      if i[j].n != "Aged Brie" # and i[j].n != "Backstage passes to a TAFKAL80ETC concert"
        if i[j].n != "Backstage passes to a TAFKAL80ETC concert"
          if i[j].q > 0
            if i[j].n != "Sulfuras, Hand of Ragnaros" 
              i[j].q = i[j].q - 1  
        else
          i[j].q = i[j].q - i[j].q
      else
        if i[j].q < 50
          i[j].q = i[j].q + 1  
        # else
        #   if i[j].n == "Aged Brie"
        #     i[j].q = i[j].q + 1  
    j++
exports.updateQuality = update_quality

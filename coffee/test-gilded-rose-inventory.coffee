should = require('chai').should()
IM = require './InventoryManager'
[i, updateQuality] = [IM.i, IM.updateQuality]
describe 'Gilded Rose', ->
  it 'there should be 6 items in the inventory', ->
    i.should.have.length 6
  it 'Comprehensive daily update teest', ->
    updateQuality i
    true.should.equal true
    # I has 100% code coverage! Job done.
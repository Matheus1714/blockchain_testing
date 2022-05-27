const PurchaseContract = artifacts.require('Purchase');

module.exports = function (deployer) {
    deployer.deploy(PurchaseContract);
};
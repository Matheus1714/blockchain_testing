const Purchase = artifacts.require("Purchase");
contract("Purchase", (accounts) => {
    let purchase;
    let expectedBuyer;
    before(async () => {
        purchase = await Purchase.deployed();
    });
    describe("get account addresses for every purchase", async () => {
        before("buy a car using accounts[0]", async () => {
            await purchase.buy(4, { from: accounts[0] });
            expectedBuyer = accounts[0];
        });
        it("can retrieve buyer's address by car id", async () => {
            const buyer = await purchase.buyers(4);
            assert.equal(buyer, expectedBuyer, "Expected to return buyer's account.");
        });
        it("can retrieve addresses of every buyers", async () => {
            const buyers = await purchase.getBuyers();
            assert.equal(buyers[4], expectedBuyer, "Buyer should be included.");
        });
    });
});
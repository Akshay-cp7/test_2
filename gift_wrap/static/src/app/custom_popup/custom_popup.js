import { Component, useState, onWillStart } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";
import { patch } from "@web/core/utils/patch";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { useService } from "@web/core/utils/hooks";

export class GiftWrapPopup extends Component {
    static template = "pos_custom.GiftWrapPopup";
    static components = { Dialog };

    setup() {
        this.orm = useService("orm");
        this.state = useState({ giftWrapProducts: [] });

        onWillStart(async () => {
            const products = await this.orm.searchRead(
                "product.product",
                [["gift_wrap", "=", true]],  
                ["id", "name", "lst_price", "image_128"]
            );
            this.state.giftWrapProducts = products;
        });
    }

    selectGiftWrap(product) {
        if (this.props.addGiftWrapToOrder) {
            this.props.addGiftWrapToOrder(product);
        }
        this.close();
    }

    close() {
        if (this.props.close) {
            this.props.close();
        }
    }
}

patch(ControlButtons.prototype, {
    async onClickPopupGiftWrap() {
        this.dialog.add(GiftWrapPopup, {
            props: { title: "Select Gift Wrap" },  // ✅ Ensure title is passed as a prop
            addGiftWrapToOrder: this.addGiftWrapToOrder.bind(this),
            close: () => this.dialog.close(),
        });
        
    },

    addGiftWrapToOrder(product) {
        const order = this.env.services.pos.get_order();
        if (order) {
            order.add_product(this.env.services.pos.db.get_product_by_id(product.id), {
                price: product.lst_price,
            });
        }
    },
});

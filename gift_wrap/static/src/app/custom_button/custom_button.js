import { Component } from "@odoo/owl";
import { patch } from "@web/core/utils/patch";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { GiftWrapPopup } from "../custom_popup/custom_popup"; // Import the popup component

patch(ControlButtons.prototype, {
    onClickPopupSingleField() {
        this.dialog.add(GiftWrapPopup, {
            title: "Select Gift Wrap",
            close: () => this.dialog.close(),
        });
    },
});

import { Component } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";
import { patch } from "@web/core/utils/patch";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";

export class EmptyPopup extends Component {
    static template = "pos_custom.EmptyPopup";
    static components = { Dialog };

    close() {
        this.props.close();

    }
}
patch(ControlButtons.prototype, {
    onClickPopupSingleField() {
        this.dialog.add(EmptyPopup, {
            title: "Popup",
            close: () => this.dialog.close(),
        });
    },
});

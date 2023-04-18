/*  Copyright Dominic Krimmer <https://www.dkrimmer.de>
    License MIT (https://opensource.org/licenses/MIT). */
    odoo.define('pos_min_price_plastinorte.pos_min_price', function (require) {
        'use strict';
    
        var models = require('point_of_sale.models');
        var screens = require('point_of_sale.screens');
    
        models.load_fields('product.product', ['min_price', 'standard_price', 'def_retal']);
        models.load_fields('pos.config', ['check_margin']);
    
        screens.PaymentScreenWidget.include({
            validate_order: function (force_validation) {
                var self = this;
                var order = this.pos.get_order();
                var lines = order.get_orderlines();
                var check_margin = this.pos.config.check_margin;
    
                if (check_margin) {
                    for (var i = 0; i < lines.length; i++) {
                        var line = lines[i];
                        
                        if (line.get_product().min_price !== undefined && 
                            line.get_product().min_price !== false && 
                            line.get_product().min_price >0 && 
                            line.quantity > line.get_product().def_retal) {
                            var product = line.get_product();
                            var taxes = product.taxes_id;
                            var tax_total = 0;
                            
                            if (taxes.length > 0) {
                                taxes.forEach(function (tax_id) {
                                    var tax = this.pos.taxes.find(function (t) {
                                        return t.id === tax_id;
                                    });
                                    if (tax) {
                                        var tax_amount = tax.amount_type === 'percent' ? (product.standard_price * (tax.amount / 100)) : tax.amount;
                                        tax_total += tax_amount;
                                    }
                                }, this);
                            }
                            
                            var min_price = (product.standard_price + tax_total) * (1 + product.min_price / 100);
                            
                            //var min_price = line.get_product().standard_price * (1 + line.get_product().min_price / 100);
                            console.log("Product:", line.get_product().display_name);
                            console.log("Standard Price:", line.get_product().standard_price);
                            console.log("Tax:", tax_total);
                            console.log("Min Price Margin:", line.get_product().min_price);
                            console.log("Min Price:", min_price);
                            console.log("Line Unit Price:", line.get_unit_price());
                            console.log("Quantity:", line.quantity);
                            console.log("POS:", line.order.pos.config.crm_team_id[1]);
                            
                            if (line.get_unit_price() < min_price) {
                                this.gui.show_popup('error', {
                                    'title': 'Error de Precio',
                                    'body': 'El precio $' + line.get_unit_price() + ' para "' + line.get_product().display_name + '" está por debajo del mínimo permitido. El Precio minimo es $' + Math.round((min_price+1).toFixed(2)) + '. Por favor, corrija el precio antes de continuar.'
                                });
                                return;
                            }
                        }
                    }
                }
                this._super(force_validation);
            },
        });
    });
        
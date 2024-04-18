const { Model } = require('objection');
const Productline = require('./Productline.js');

class Product extends Model {

    static get tableName() {
        return 'products';
    }

    static get idColumn() {
        return 'productCode';
    }


    static get jsonSchema() {
        return {
            type: 'object',
            required: [],

            properties: {
                productCode: { type: 'string' },
                productName: { type: 'string' },
                productLine: { type: 'string' },
                productScale: { type: 'string' },
                productVendor: { type: 'string' },
                productDescription: { type: 'string' },
                quantityInStock: { type: 'number' },
                buyPrice: { type: 'string' },
                MSRP: { type: 'string' },
            
            }
        };
    }
    static get relationMappings() {
      
        return {
          productline: {
                    relation: Model.ManyToManyRelation,
                    modelClass: Productline,
                    join: {
                        from: 'products.productLine',
                        to: 'productlines.productLine'
                    }
                }
        };
    }
}

module.exports = Product;

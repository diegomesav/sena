const model = require('../models/products')

exports.getData = (req,res) => {

    model.find().then((docs) => {
        res.send({
            docs:docs
        })
    })
}


exports.insertData = async (req, res) => {

  try {
    const newItem = req.body;
    console.log(newItem)
    const createdItem = await model.create(newItem);
    res.status(201).json(createdItem);
  } catch (error) {
    res.status(500).json({ error: 'Error al crear el producto' });
    console.log(error)
  }
};

exports.getSomeData = async (req, res) => {
  const id = req.params.id;//para buscar directamente por el Id Generado por MongoDB
  console.log(id);
  //const avatar = req.params.avatar;//Para buscar por cualquier valor del esquema
  ///console.log(avatar);
  try {
    const item = await model.findById(id); //para buscar directamente por el Id Generado por MongoDB
    console.log(item);
    if (item) {
      res.json(item);
//************************************************************************************************************************** */
    /*const items = await model.find({avatar:avatar}); //para buscar todos los elementos que cumplan un criterio del esquema
    console.log(items);
    if (items) {
      res.json(items);*/
    } else {
      console.log(res.status(404).json({ error: 'producto no encontrado' }));

    }
  } catch (error) {
    console.log('Error en catch:',error);
    res.status(500).json({ error: 'Error al obtener el producto' });
  }
};

exports.updatedItem = async (req, res) => {
  const id = req.params.id;
  const updatedItem = req.body;
  try {
    const result = await model.findByIdAndUpdate(id, updatedItem, { new: true });
    if (result) {
      res.json(result);
    } else {
      res.status(404).json({ error: 'producto no encontrado' });
    }
  } catch (error) {
    console.log(error)
    res.status(500).json({ error: 'Error al actualizar el producto' });
  }
};

exports.deleteUser = async (req, res) => {
  const id = req.params.id;
  try {
    const result = await model.findByIdAndDelete(id);
    if (result) {
      res.sendStatus(204);
    } else {
      console.log(res.status(404).json({ error: 'producto no encontrado' }));
    }
  } catch (error) {
    console.log(error)
    res.status(500).json({ error: 'Error al eliminar el producto' });
  }
};


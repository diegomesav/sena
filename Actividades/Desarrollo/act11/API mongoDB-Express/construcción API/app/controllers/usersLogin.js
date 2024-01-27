//ChatGPT

const express = require('express');
const router = express.Router();
const bcrypt = require('bcrypt');

const User = require('../models/usersLogin')

exports.insertData = async (req, res) => {

  const { name, email, password } = req.body;

  try {
    // Verificar si el usuario ya existe en la base de datos
    const existingUser = await User.findOne({ email: email });
    if (existingUser) {
      return res.status(400).json({ error: 'El usuario ya existe' });
    }

    // Hash de la contraseña antes de almacenarla en la base de datos
    const hashedPassword = await bcrypt.hash(password, 10);

    // Crear un nuevo usuario
    const newUser = new User({
      name: name,
      email: email,
      password: hashedPassword,
    });

    // Guardar el usuario en la base de datos
    const savedUser = await newUser.save();

    res.status(201).json(savedUser);
  } catch (error) {
    console.error('Error durante el registro:', error);
    res.status(500).json({ error: 'Error al registrar el usuario' });
  }
};

exports.login = async (req, res) => {
  const { email, password } = req.body;
  console.log(email)
  try {
    // Buscar el usuario en la base de datos
    const user = await User.findOne({ email: email });
    console.log(user)
    if (!user) {
      return res.status(401).json({ error: 'El usuario no existe' });
    }

    // Verificar la contraseña
    const passwordMatch = await bcrypt.compare(password, user.password);
    if (!passwordMatch) {
      return res.status(401).json({ error: 'Contraseña incorrecta' });
    }

    res.json({ message: 'Inicio de sesión exitoso' });
  } catch (error) {
    console.error('Error durante el inicio de sesión:', error);
    res.status(500).json({ error: 'Error al iniciar sesión' });
  }
};




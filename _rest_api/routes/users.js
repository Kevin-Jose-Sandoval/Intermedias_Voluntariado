const { Router } = require('express');
const { getUsers, createUser, getUser, deleteUser, updateUser } = require('../controllers/users');
const router = new Router();


router.get('/users', getUsers);

router.get('/users/:id', getUser);

router.post('/users', createUser);

router.delete('/users/:id', deleteUser);

router.patch('/users/:id', updateUser);

module.exports = router;
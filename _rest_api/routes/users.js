const { Router } = require('express');
const router = new Router();

const data = require('../data.json')

router.get('/', (req, res) => {
    res.status(200).json(data)
});

router.post('/users', (req, res) => {
    const id = data.length + 1;
    const new_user = {id, ...req.body};

    data.push(new_user)
    res.json(data)
});

router.delete('/users/:id', (req, res) => {
    const id = req.params.id;
    let found_id = false;

    for (let i = 0; i < data.length; i++){
        if (data[i].id == id){
            data.splice(i, 1);
            found_id = true;
        }
    }

    if (!found_id){
        res.status(404).json({error : "User id not found"});
    }else {
        res.json(data)
    }
});

module.exports = router;
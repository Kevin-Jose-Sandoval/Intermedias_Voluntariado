const { v4 } = require('uuid')
let data = []

const getUsers = (req, res) => {
    res.status(200).json(data)
}

const getUser = (req, res) => {
    const { id } = req.params;

    const foundUser = data.find((user) => 
        user.id == id
    )

    if (foundUser == undefined){
        res.status(404).json({error : "User id not found"});
    }else {
        res.status(200).json(foundUser)
    }    
};

const createUser = (req, res) => {
    const new_user = req.body;

    const user_with_id = { ...new_user, id: v4() }
    data.push(user_with_id)

    res.status(201).json('User with the name ' + new_user.firstName + ' added to data')
};

const deleteUser =  (req, res) => {
    const { id } = req.params;

    data = data.filter((user) => user.id != id);

    res.status(200).json('User with the id ' + id + ' deleted to data');
};

const updateUser = (req, res) => {
    const { id } = req.params;
    const { firstName, lastName, age } = req.body;
    
    const user = data.find((user) => user.id == id)

    if (user != undefined){
        if(firstName) user.firstName = firstName;
        if(lastName) user.lastName = lastName;
        if(age) user.age = age;
    
        res.status(201).json('User with the id ' + id + ' has been updated');
    } else {
        res.status(404).json({error : "User id not found"});
    }

};

module.exports = {
    getUsers,
    getUser,
    createUser,
    deleteUser,
    updateUser
}
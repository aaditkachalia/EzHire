import React,{useState} from 'react';

const Auth() => {

const [auth, setAuthen] = useState("false")
const [user, setUsername] = useState("")


const setAuth(){
	setAuthen("true")
}

const getAuth(){
	return auth
}

const setUser(name){
	setUsername(name)
}

const getUser(name){
	return user
}
}

export Auth
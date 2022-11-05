import React from 'react'
import UserInfoType from './userInfoSlice'

function userInfoView(user:UserInfoType) {
    return <h1>{user}</h1>; //TODO
}

export default React.memo(userInfoView);
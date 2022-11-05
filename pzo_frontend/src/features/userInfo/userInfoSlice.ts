import type { PayloadAction } from '@reduxjs/toolkit'
import { createSlice } from '@reduxjs/toolkit'

export interface UserInfoType {
  email: string
}

const initialState: UserInfoType = {
  email: '',
}

const userInfoSlice = createSlice({
  name: 'userInfo',
  initialState,
  reducers: {
    userInfoFetched(state: UserInfoType, action: PayloadAction<UserInfoType>) {
      return action.payload
    },
  },
})

export const { userInfoFetched } =
  userInfoSlice.actions
export default userInfoSlice.reducer

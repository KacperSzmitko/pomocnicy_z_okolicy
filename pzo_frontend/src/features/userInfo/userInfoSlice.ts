import type { PayloadAction } from '@reduxjs/toolkit'
import { createSlice } from '@reduxjs/toolkit'

export interface UserInfoType {
  email: string;
  firstname: string;
  surname: string;
  age: number;
  city: string;
  points: number;
  search_area: number;
}

const initialState: UserInfoType = {
  email: "",
  firstname: "",
  surname: "",
  age: 0,
  city: "",
  points: 0,
  search_area: 0,
};

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

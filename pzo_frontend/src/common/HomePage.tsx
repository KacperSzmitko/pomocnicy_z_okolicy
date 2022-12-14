import { useEffect, useState } from 'react'
import { refresh_cookie_token, logout } from '../features/auth/authActions'
import { Outlet, useNavigate, useLocation, Link } from 'react-router-dom'

import { useAppDispatch } from './hooks'
import { getUserInfo } from '../features/userInfo/actions'
import { getReportTypes } from "../features/reports/actions";

interface CustomizedState {
  tokenStatus: number
}

export default function HomePage() {
  const location = useLocation()
  const [tokenStatus, setTokenStatus] = useState(0)
  const navigate = useNavigate()
  const dispach = useAppDispatch()

  useEffect(() => {
    // State is set if there was a redirection
    const state = location.state as CustomizedState
    if (state) {
      setTokenStatus(state.tokenStatus)
    } else {
      refresh_cookie_token().then((response) => setTokenStatus(response.status))
    }
  }, [])

  useEffect(() => {
    if (tokenStatus === 200) {
      dispach(getUserInfo());
      dispach(getReportTypes());
    } else if (tokenStatus === 401) {
      navigate('/login', { state: { tokenStatus } })
    }
  }, [tokenStatus])

  async function logOut() {
    const response = await logout()
    if (response.status === 200) {
      navigate('/login')
    }
  }

  if (tokenStatus === 200) {
    return (
      <div>
        Zalogowano
        <button onClick={logOut}>Wyloguj</button>
        <br />
        <Link to="">Strona główna</Link> <br />
        <Link to="/notifications">Powiadomienia</Link> <br />
        <Outlet />
      </div>
    )
  }

  return <div></div>
}

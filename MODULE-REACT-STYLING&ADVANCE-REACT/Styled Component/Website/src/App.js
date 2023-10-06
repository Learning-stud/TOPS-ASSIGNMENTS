import Header from './Componenet/Header';
import Fotter from './Componenet/Fotter'
import Home from './gg/Home';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import About from './gg/About';
import SignUp from './gg/SignUp';
import Service from './gg/Service';
import OurGallery from './gg/OurGallery';
import { ToastContainer } from 'react-toastify';
import "react-toastify/dist/ReactToastify.css"
import Login from './gg/login';
import UserProfile from './gg/UserProfile';
function App() {
  return (
    <BrowserRouter>
      <ToastContainer></ToastContainer>
      <Routes>
        <Route path='/' element={<> <Header /> <Home /> <Fotter /> </>} ></Route>
        <Route path='/About' element={<> <Header /> <About /> <Fotter /> </>} ></Route>
        <Route path='/OurGallery' element={<> <Header /> <OurGallery /> <Fotter /> </>} ></Route>
        <Route path='/Service' element={<> <Header /> <Service/> <Fotter /> </>} ></Route>
        <Route path='/SignUp' element={<> <Header /> <SignUp/> <Fotter /> </>} ></Route>
        <Route path='/Login' element={<> <Header /> <Login/> <Fotter /> </>} ></Route>
        <Route path='/UserProfile' element={<> <Header /> <UserProfile/> <Fotter /> </>} ></Route>
      </Routes>

    </BrowserRouter>
  );
}

export default App;
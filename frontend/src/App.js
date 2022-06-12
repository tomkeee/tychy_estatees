import Header from "./components/Header";
import Offers from "./components/Offers";
import Container from "react-bootstrap/Container"
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";


function App() {
  return (
    <Router>
      <Header />
      <Container>
        <Routes>

          <Route
            path="/oferty"
            element={
              <Offers />
            }
          />
            
        </Routes>
      </Container>
    </Router>
  );
}

export default App;

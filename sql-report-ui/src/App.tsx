import EmployeeReportTable from "./components/EmployeeReportTable";
import Finances from "./components/Finances";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="min-h-screen w-full text-zinc-50 bg-zinc-800 flex items-center justify-center">
      <BrowserRouter>
        <Routes>
          <Route path="/employees" element={<EmployeeReportTable />} />
          <Route path="/finances" element={<Finances />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

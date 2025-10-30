import { useEffect, useState } from "react";
import { fetchEmployees } from "../services/api";

type Employee = {
  id: number;
  name: string;
  department: string;
  salary: number;
  performance: number;
};

export default function EmployeeReportTable() {
  const [data, setData] = useState<Employee[]>([]);
  const [filtered, setFiltered] = useState<Employee[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [search, setSearch] = useState("");

  useEffect(() => {
    async function loadReport() {
      try {
        const result = await fetchEmployees();
        setData(result.results);
        setFiltered(result.results);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadReport();
  }, []);

  useEffect(() => {
    const lower = search.toLowerCase();
    setFiltered(
      data.filter(
        (e) =>
          e.name.toLowerCase().includes(lower) ||
          e.department.toLowerCase().includes(lower)
      )
    );
  }, [search, data]);

  if (loading)
    return <p className="text-center text-gray-500">Carregando...</p>;
  if (error) return <p className="text-center text-red-500">{error}</p>;

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <h1 className="text-2xl font-bold mb-6 text-center">
        Relatório de Funcionários
      </h1>

      <input
        type="text"
        placeholder="🔍 Buscar por nome ou departamento..."
        className="w-full mb-4 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <div className="overflow-x-auto rounded-lg shadow">
        <table className="min-w-full border-collapse bg-white">
          <thead className="bg-gray-100 sticky top-0">
            <tr>
              {["ID", "Nome", "Departamento", "Salário", "Performance"].map(
                (title) => (
                  <th
                    key={title}
                    className="border-b px-4 py-2 text-left font-semibold text-gray-700"
                  >
                    {title}
                  </th>
                )
              )}
            </tr>
          </thead>
          <tbody>
            {filtered.map((e, i) => (
              <tr
                key={e.id}
                className={`${
                  i % 2 === 0 ? "bg-gray-50" : "bg-white"
                } hover:bg-blue-50 transition`}
              >
                <td className="border-b px-4 py-2">{e.id}</td>
                <td className="border-b px-4 py-2">{e.name}</td>
                <td className="border-b px-4 py-2">{e.department}</td>
                <td className="border-b px-4 py-2">
                  R$ {e.salary.toLocaleString("pt-BR")}
                </td>
                <td className="border-b px-4 py-2">{e.performance}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <p className="text-sm text-gray-500 mt-3 text-center">
        Total: {filtered.length} funcionários
      </p>
    </div>
  );
}

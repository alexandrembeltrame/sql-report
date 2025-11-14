import { useEffect, useState } from "react";
import { fetchFinances } from "../services/api";

interface Finance {
  id: number;
  date: string;
  description: string;
  doc_number: string;
  credit: number;
  debit: number;
}

export default function Finances() {
  const [finances, setFinances] = useState<Finance[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadFinances() {
      try {
        const data = await fetchFinances();
        setFinances(data.results ?? data);
        console.log("💰 Finances:", data);
      } catch (error) {
        console.error("Erro ao carregar finanças", error);
      } finally {
        setLoading(false);
      }
    }
    loadFinances();
  }, []);

  if (loading) return <p>Carregando...</p>;

  if (finances.length === 0)
    return (
      <p className="text-center mt-10">Nenhum dado financeiro disponível.</p>
    );

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">📊 Relatório Financeiro</h1>
      <table className="table-auto border-collapse w-full border border-gray-300">
        <thead>
          <tr className="bg-gray-800 text-white">
            <th className="border p-2">Data</th>
            <th className="border p-2">Descrição</th>
            <th className="border p-2">DOC</th>
            <th className="border p-2">Crédito</th>
            <th className="border p-2">Débito</th>
          </tr>
        </thead>
        <tbody>
          {finances.map((item) => (
            <tr key={item.id}>
              <td className="border p-2">
                {new Date(item.date).toLocaleString("pt-BR")}
              </td>
              <td className="border p-2">
                {item.description.toLocaleString()}
              </td>
              <td className="border p-2">
                R$ {item.doc_number.toLocaleString()}
              </td>
              <td className="border p-2 text-green-400">
                {item.credit.toLocaleString("pt-BR", {
                  style: "currency",
                  currency: "BRL",
                })}
              </td>
              <td className="border p-2 text-green-400">
                {item.debit.toLocaleString("pt-BR", {
                  style: "currency",
                  currency: "BRL",
                })}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

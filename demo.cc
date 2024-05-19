#include <pybind11/pybind11.h>
#include <arrow/api.h>
#include <arrow/python/pyarrow.h>

int num_rows(pybind11::object const & py_obj) {
	auto result = arrow::py::unwrap_table(py_obj.ptr());
	if (not result.ok()) {
		throw std::runtime_error("argument must be an Arrow table");
	}
	std::shared_ptr<arrow::Table> table = result.ValueOrDie();
	return table->num_rows();
}

PYBIND11_MODULE(demo, m)
{
	arrow::py::import_pyarrow();
  m.def("num_rows", &num_rows);
}

class FormRegister extends React.Component {
  const;
  state = {
    email: "",
    name: "",
    password: "",
    isEmailValid: false,
    isEmailExist: false,
    isLoading: false,
    isSuccess: false
  };

  handleChange = e => {
    const { name, value } = e.target;
    const { isEmailValid } = this.state;
    const rgx = /^\w+([\\.-]?\w+)*@\w+([\\.-]?\w+)*(\.\w{2,3})+$/;
    this.setState(
      {
        [name]: value,
        isEmailValid: name === "email" ? rgx.test(value) : isEmailValid,
        isSuccess: false
      },
      () => {
        if (name === "email" && isEmailValid) this.checkEmail(this.state.email);
      }
    );
  };

  checkEmail = async email => {
    const { body } = await superagent
      .post("/api/check-email/")
      .set("X-CSRFToken", this.props.token)
      .set("content-type", "application/json")
      .send({ email: email });
    this.setState({ isEmailExist: body.exist });
  };

  handleSubmit = async (e, canSubmit) => {
    e.preventDefault();
    const { email, name, password } = this.state;
    if (canSubmit) {
      this.setState({ isLoading: true });
      const { body } = await superagent
        .post("/api/register/")
        .set("X-CSRFToken", this.props.token)
        .set("content-type", "application/json")
        .send({ email: email, name: name, password: password });
      this.setState({
        isSuccess: body.success,
        isLoading: false,
        email: "",
        name: "",
        password: "",
        isEmailValid: false,
        isEmailExist: false
      });
    }
  };

  render() {
    const {
      email,
      name,
      password,
      isEmailValid,
      isEmailExist,
      isLoading,
      isSuccess
    } = this.state;

    const canSubmit =
      isEmailValid &&
      email.length !== 0 &&
      name.length !== 0 &&
      password.length !== 0 &&
      !isEmailExist;

    return (
      <form onSubmit={e => this.handleSubmit(e, canSubmit)}>
        <div className="form-group">
          {isSuccess && (
            <div className="alert alert-success">Berhasil Mendaftar</div>
          )}
          <label for="name">Email: </label>
          <input
            type="email"
            className="form-control"
            id="email"
            placeholder="Masukkan email"
            name="email"
            maxlength="50"
            value={email}
            onChange={e => this.handleChange(e)}
            required
          />
          {email.length !== 0 && !isEmailValid && (
            <div className="alert alert-danger">Format email salah</div>
          )}
          {isEmailExist && (
            <div className="alert alert-danger">
              Email sudah pernah didaftarkan
            </div>
          )}
        </div>
        <div className="form-group">
          <label for="name">Nama: </label>
          <input
            type="text"
            className="form-control"
            id="name"
            placeholder="Masukkan nama"
            name="name"
            maxlength="50"
            value={name}
            onChange={e => this.handleChange(e)}
            required
          />
        </div>
        <div className="form-group">
          <label for="name">Password: </label>
          <input
            type="password"
            className="form-control"
            id="password"
            placeholder="Masukkan password"
            name="password"
            maxlength="50"
            value={password}
            onChange={e => this.handleChange(e)}
            required
          />
        </div>
        <button
          type="submit"
          id="submit"
          className="btn btn-default"
          disabled={!canSubmit || isLoading}
        >
          {isLoading ? <i className="fas fa-circle-notch fa-spin" /> : "Submit"}
        </button>
      </form>
    );
  }
}

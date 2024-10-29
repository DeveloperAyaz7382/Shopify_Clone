import React, { useState } from 'react';
import { Form, Input, Button, message } from 'antd';
import axios from 'axios';

const LoginForm = () => {
  const [loading, setLoading] = useState(false);

  const onFinish = async (values) => {
    setLoading(true);
    try {
      // Send the email and password to the backend
      const response = await axios.post('http://127.0.0.1:8000/login', values);
      message.success('Login successful!');
    } catch (error) {
      message.error('Login failed. Check your credentials!');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Form name="login" onFinish={onFinish} layout="vertical">
      <Form.Item
        name="email"
        label="Email"
        rules={[{ required: true, type: 'email' }]}
      >
        <Input />
      </Form.Item>
      <Form.Item
        name="password"
        label="Password"
        rules={[{ required: true }]}
      >
        <Input.Password />
      </Form.Item>
      {/* Optionally, include a name field here if desired */}
      {/* <Form.Item
        name="name"
        label="Name"
        rules={[{ required: true, message: 'Please enter your name!' }]}
      >
        <Input />
      </Form.Item> */}
      <Form.Item>
        <Button type="primary" htmlType="submit" loading={loading}>
          Login
        </Button>
      </Form.Item>
    </Form>
  );
};

export default LoginForm;

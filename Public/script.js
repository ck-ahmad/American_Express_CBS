// Premium Banking App - JavaScript

// Initialize data from localStorage or use defaults
const initData = () => {
  if (!localStorage.getItem('customers')) {
    localStorage.setItem('customers', JSON.stringify([
      {
        id: "CUST001",
        name: "John Doe",
        email: "john.doe@email.com",
        phone: "+92 300 1234567",
        address: "123 Main Street, Karachi",
        joinDate: "2024-01-15"
      },
      {
        id: "CUST002",
        name: "Jane Smith",
        email: "jane.smith@email.com",
        phone: "+92 321 9876543",
        address: "456 Park Avenue, Lahore",
        joinDate: "2024-02-20"
      },
      {
        id: "CUST003",
        name: "Mike Johnson",
        email: "mike.j@email.com",
        phone: "+92 333 5551234",
        address: "789 Garden Road, Islamabad",
        joinDate: "2024-03-10"
      }
    ]));
  }

  if (!localStorage.getItem('accounts')) {
    localStorage.setItem('accounts', JSON.stringify([
      {
        accountNo: "ACC12345678",
        customerId: "CUST001",
        type: "Savings",
        balance: 125000.00
      },
      {
        accountNo: "ACC87654321",
        customerId: "CUST002",
        type: "Current",
        balance: 350000.50
      },
      {
        accountNo: "ACC45678912",
        customerId: "CUST001",
        type: "Fixed",
        balance: 500000.00
      }
    ]));
  }

  if (!localStorage.getItem('transactions')) {
    localStorage.setItem('transactions', JSON.stringify([
      {
        id: "TXN001",
        accountNo: "ACC12345678",
        type: "Deposit",
        amount: 50000,
        date: "2024-11-22",
        time: "10:30 AM",
        status: "Completed"
      },
      {
        id: "TXN002",
        accountNo: "ACC87654321",
        type: "Withdrawal",
        amount: 15000,
        date: "2024-11-22",
        time: "11:45 AM",
        status: "Completed"
      },
      {
        id: "TXN003",
        accountNo: "ACC12345678",
        type: "Transfer",
        amount: 25000,
        date: "2024-11-21",
        time: "03:15 PM",
        status: "Completed"
      }
    ]));
  }

  if (!localStorage.getItem('logs')) {
    localStorage.setItem('logs', JSON.stringify([
      {
        id: "LOG001",
        action: "Account Created",
        user: "Admin",
        details: "New savings account for CUST001",
        timestamp: "2024-11-22 10:30:45",
        status: "success"
      },
      {
        id: "LOG002",
        action: "Transaction Processed",
        user: "System",
        details: "Deposit of PKR 50,000 to ACC12345678",
        timestamp: "2024-11-22 11:15:22",
        status: "success"
      },
      {
        id: "LOG003",
        action: "Customer Added",
        user: "Admin",
        details: "New customer registered: John Doe",
        timestamp: "2024-11-22 09:45:10",
        status: "success"
      },
      {
        id: "LOG004",
        action: "Failed Login Attempt",
        user: "Unknown",
        details: "Invalid credentials from IP 192.168.1.100",
        timestamp: "2024-11-22 08:20:33",
        status: "warning"
      },
      {
        id: "LOG005",
        action: "Transaction Failed",
        user: "System",
        details: "Insufficient funds in ACC87654321",
        timestamp: "2024-11-21 16:55:18",
        status: "error"
      }
    ]));
  }
};

// Toast notification
const showToast = (message, type = 'success') => {
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  
  const icon = type === 'success' 
    ? '<svg class="toast-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>'
    : '<svg class="toast-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"></path></svg>';
  
  toast.innerHTML = `
    ${icon}
    <span>${message}</span>
  `;
  
  document.body.appendChild(toast);
  
  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
};

// Format currency
const formatCurrency = (amount) => {
  return `PKR ${parseFloat(amount).toLocaleString('en-PK', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
};

// Format date
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
};

// Add log entry
const addLog = (action, details, status = 'success') => {
  const logs = JSON.parse(localStorage.getItem('logs') || '[]');
  const now = new Date();
  
  const newLog = {
    id: `LOG${(logs.length + 1).toString().padStart(3, '0')}`,
    action,
    user: "Admin",
    details,
    timestamp: now.toISOString().slice(0, 19).replace('T', ' '),
    status
  };
  
  logs.unshift(newLog);
  localStorage.setItem('logs', JSON.stringify(logs));
};

// Set active nav link
const setActiveNav = () => {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href');
    if ((currentPage === 'index.html' && href === 'index.html') ||
        (currentPage !== 'index.html' && href === currentPage)) {
      link.classList.add('active');
    }
  });
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  initData();
  setActiveNav();
});

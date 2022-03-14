/// <reference types="cypress" />

describe('Newsletter Test', function() 
{
    before(function() {
        // runs once before all tests in the block
        cy.fixture('data').then(function(data)
        {
            this.data = data;
        })
   })

   beforeEach(() => {    
    Cypress.Cookies.preserveOnce('session_id', 'remember_token')
  })

it('displays login page', () => {

    // Cypress launch newsletter URL
    cy.visit(Cypress.env('url'))

    // Check if the login page is displayed
    cy.get('.btn.btn-success').should('be.visible').contains('Sign in')
   
})

it('click on login link', () => {
    
        // Click on login link
        cy.get('.btn.btn-success').click()
    })

it('Enter email id', () => {
    // Enter email id'
    cy.get("input[type='email']").type('test@qxf2.com')
})

it('should have next button', () => {

    // Check if the next button is displayed
    cy.get("button[class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b'] div[class='VfPpkd-RLmnJb']").should('be.visible')
    cy.get('button').contains('Next').click()

    
})

})